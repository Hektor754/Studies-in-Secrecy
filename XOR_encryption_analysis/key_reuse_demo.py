import base64

def XOR_bytes(b1, b2):
    return bytes([x ^ y for x, y in zip(b1, b2)])

with open("message1.otp.enc", "rb") as f1:
    c1 = base64.b64decode(f1.read())

with open("message2.otp.enc", "rb") as f2:
    c2 = base64.b64decode(f2.read())

xor_of_ciphertexts = XOR_bytes(c1, c2)

with open("xor_leak.bin", "wb") as f_out:
    f_out.write(xor_of_ciphertexts)