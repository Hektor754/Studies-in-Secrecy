import base64

def OTP_decryption(encrypted_bytes, key_bytes):
    decrypted = bytes([e ^ k for e, k in zip(encrypted_bytes, key_bytes)])
    return decrypted

file = input("Specify the base filename for decryption (without extensions): ")

with open(file + '.otp.enc', 'rb') as f_enc:
    encrypted = base64.b64decode(f_enc.read())

with open(file + '.otp.key', 'rb') as f_key:
    key = base64.b64decode(f_key.read())

if len(encrypted) != len(key):
    raise ValueError("Key length must match message length for OTP")

decrypted = OTP_decryption(encrypted, key)

try:
    print(decrypted.decode('utf-8'))
except UnicodeDecodeError:
    print("Decrypted content is binary or not valid UTF-8.")