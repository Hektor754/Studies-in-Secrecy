import os
import base64

def XOR_encryption(content_bytes):
    key = os.urandom(64)
    repeated_key = (key * (len(content_bytes) // len(key))) + key[:len(content_bytes) % len(key)]
    encrypted = bytes([b ^ k for b, k in zip(content_bytes, repeated_key)])
    return key, encrypted


file = input("Specify the file path: ")

with open(file, 'rb') as f:
    message = f.read()

key, encrypted = XOR_encryption(message)
encoded_encrypted = base64.b64encode(encrypted)
encoded_key = base64.b64encode(key)

with open(file + ".enc", 'wb') as f_enc:
    f_enc.write(encoded_encrypted)

with open(file + ".key", 'wb') as f_key:
    f_key.write(encoded_key)

