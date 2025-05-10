import os
import base64

def OTP_encryption(content_bytes):
    key = os.urandom(len(content_bytes))
    encrypted = bytes([b ^ k for b, k in zip(content_bytes, key)])
    return key, encrypted


file = input("Specify the file path: ")

with open(file, 'rb') as f:
    message = f.read()

key, encrypted = OTP_encryption(message)

with open(file + ".otp.enc", 'wb') as f_enc:
    f_enc.write(base64.b64encode(encrypted))

with open(file + '.otp.key', 'wb') as f_key:
    f_key.write(base64.b64encode(key))