import os
import base64

#Lets say we do not generate a new OTP key every time we encrypt and we instead use the same one

def OTP_encryption(content_bytes,key):
    encrypted = bytes([b ^ k for b, k in zip(content_bytes, key)])
    return encrypted


file = input("Specify the file path: ")

with open(file, 'rb') as f:
    message = f.read()

with open(file + '.otp.key', 'rb') as f_key:
    key = base64.b64decode(f_key.read())

encrypted = OTP_encryption(message,key)

with open(file + ".otp.enc", 'wb') as f_enc:
    f_enc.write(base64.b64encode(encrypted))