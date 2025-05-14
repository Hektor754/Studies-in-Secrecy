import os
import json
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
    
    # Save keys to files
    with open("public_key.txt", "w") as pub_file:
        pub_file.write(json.dumps({"n": n, "e": e}))

    with open("private_key.txt", "w") as priv_file:
        priv_file.write(json.dumps({"n": n, "d": d}))
    
    print("Keys generated and saved.")
    return (n, e, d)

def load_keys():
    if not os.path.exists("public_key.txt") or not os.path.exists("private_key.txt"):
        print("Keys not found. Generating new keys...")
        return generate_rsa_keys()

    with open("public_key.txt", "r") as pub_file:
        public_key = json.load(pub_file)
    
    with open("private_key.txt", "r") as priv_file:
        private_key = json.load(priv_file)

    return (public_key["n"], public_key["e"], private_key["d"])

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