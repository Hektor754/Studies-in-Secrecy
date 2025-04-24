def ceasar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            result += shifted_char
        elif char.isdigit():
            shifted_num = str((int(char) + shift) % 10)
            result += shifted_num
        else:
            result += char
    return result

file = input("Specify file path or name: ")
shift = 3

with open(file, 'r+') as f:
    content = f.read()
    enc_content = ceasar_encrypt(content,shift)
    f.seek(0)
    f.write(enc_content)
    f.truncate()

print(enc_content)