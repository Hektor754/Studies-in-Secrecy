from math import gcd
import random
import secrets
import time

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
    print(f"Generating a {bits}-bit prime number...")
    start_time = time.time()

    while True:
        number = secrets.randbits(bits)
        number |= (1 << (bits - 1)) | 1

        if miller_rabin_test(number, trials):
            end_time = time.time()
            print(f"Prime found in {end_time - start_time:.2f} seconds.")
            return number

def generate_rsa_keys(bits=2048):
    prime = generate_large_prime(bits, 50)
    prime2 = generate_large_prime(bits, 50)

    while prime == prime2:
        prime2 = generate_large_prime(bits, 50)

    n = prime * prime2
    phi_n = (prime - 1) * (prime2 - 1)
    
    e = 65537
    while gcd(e, phi_n) != 1:
        e = random.randint(10000, 100000)

    print("Public Exponent e is coprime with φ(n)")
    d = pow(e, -1, phi_n)
    return (n, e, d), (n, e), (n, d)

def rsa_encryption(text: str, public_key: tuple):
    n, e = public_key
    text_int = int.from_bytes(text.encode(), 'big')
    if text_int >= n:
        raise ValueError("Message too big for this mod")
    ciphertext = pow(text_int, e, n)
    return ciphertext

def rsa_decryption(ciphertext: int, private_key: tuple) -> str:
    n, d = private_key
    text_int = int(pow(ciphertext, d, n))
    byte_length = (text_int.bit_length() + 7) // 8
    text_bytes = text_int.to_bytes(byte_length, 'big')
    text = text_bytes.decode('utf-8')
    return text