from math import gcd
import random
import secrets
import base64

def miller_rabin_test(n, k):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

def generate_large_prime(bits, trials):
    while True:
        number = secrets.randbits(bits) | 1
        if miller_rabin_test(number, trials):
            return number

def generate_rsa_keys(bits=2048):
    prime1 = generate_large_prime(bits, 50)
    prime2 = generate_large_prime(bits, 50)

    while prime1 == prime2:
        prime2 = generate_large_prime(bits, 50)

    n = prime1 * prime2
    phi_n = (prime1 - 1) * (prime2 - 1)
    
    e = 65537
    while gcd(e, phi_n) != 1:
        e = random.randint(10000, 100000)

    d = pow(e, -1, phi_n)
    
    save_key_to_pem("private_key.pem", d, n, "PRIVATE")
    save_key_to_pem("public_key.pem", e, n, "PUBLIC")

    return n, e, d

def save_key_to_pem(filename, e_or_d, n, key_type="PUBLIC"):
    """Serialize the keys to PEM format"""
    key_data = f"{e_or_d}:{n}".encode()

    base64_key = base64.b64encode(key_data).decode('utf-8')

    if key_type == "PUBLIC":
        header_footer = f"-----BEGIN PUBLIC KEY-----\n{base64_key}\n-----END PUBLIC KEY-----"
    else:
        header_footer = f"-----BEGIN PRIVATE KEY-----\n{base64_key}\n-----END PRIVATE KEY-----"

    with open(filename, "w") as pem_file:
        pem_file.write(header_footer)

    print(f"{key_type} key saved as {filename}")
    
def load_key_from_pem(filename):
    with open(filename, "r") as pem_file:
        pem_data = pem_file.read()

    base64_key = pem_data.splitlines()[1]

    decoded_data = base64.b64decode(base64_key).decode()

    e_or_d, n = map(int, decoded_data.split(':'))

    return e_or_d, n

def rsa_encryption(message: str, e: int, n: int) -> int:
    message_bytes = message.encode('utf-8')
    message_int = int.from_bytes(message_bytes, 'big')
    ciphertext = pow(message_int, e, n)
    return ciphertext

def rsa_decryption(ciphertext: int, n: int, d: int) -> str:
    text_int = pow(ciphertext, d, n)
    byte_length = (text_int.bit_length() + 7) // 8
    text_bytes = text_int.to_bytes(byte_length, 'big')
    return text_bytes.decode('utf-8')