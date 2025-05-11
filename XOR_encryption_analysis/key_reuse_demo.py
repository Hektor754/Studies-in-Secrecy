import base64

def XOR_bytes(b1, b2):
    return bytes([x ^ y for x, y in zip(b1, b2)])

with open("XOR_encryption_analysis/message1.otp.enc", "rb") as f1:
    c1 = base64.b64decode(f1.read())

with open("XOR_encryption_analysis/message2.otp.enc", "rb") as f2:
    c2 = base64.b64decode(f2.read())

xor_of_ciphertexts = XOR_bytes(c1, c2)

with open("xor_leak.bin", "wb") as f_out:
    f_out.write(xor_of_ciphertexts)

'''
The output might not be readable but it gives a valuable insight if ms1 is just msg1 XOR key and msg2 is ms2 XOR key then
msg1 XOR msg2 = (msg1 XOR key) XOR (msg2 XOR key) = msg1 XOR msg2. But what does that tell us? Well it tells us that
practically if we guess for example a word in msg1 like "The " we can actually XOR the word with the .bin file and we will
get the first 4 bytes of msg2, also known as the crib-dragging technique is the exact reason on why we can NEVER reuse keys

'''