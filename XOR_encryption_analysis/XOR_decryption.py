import os 
import base64

def XOR_decryption(message, key):
    repeated_key = (key * (len(message) // len(key))) + key[:len(message) % len(key)]
    decrypted = bytes([b ^ k for b, k in zip(message, repeated_key)])
    return decrypted

file_path = input("Specify the file path for decryption (without .enc extension): ")

with open(file_path + ".enc", 'rb') as f_enc:
    encoded_encrypted_message = f_enc.read()

with open(file_path + ".key", 'rb') as f_key:
    encoded_key = f_key.read()

encrypted_message = base64.b64decode(encoded_encrypted_message)
key = base64.b64decode(encoded_key)

decrypted_message = XOR_decryption(encrypted_message, key)

try:
    print(decrypted_message.decode('utf-8'))
except UnicodeDecodeError:
    print("The decrypted message is not a valid UTF-8 text.")