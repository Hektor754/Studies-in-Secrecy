def decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - base - shift) % 26 + base)
            result += shifted_char
        elif char.isdigit():
            shifted_num = str((int(char) - shift) % 10)
            result += shifted_num
        else:
            result += char
    return result

file = input("Specify file path or name: ")
shift = 3

with open(file, 'r+') as f:
    d_content = f.read()
    dec_content = decrypt(d_content,shift)
    f.seek(0)
    f.write(dec_content)
    f.truncate()

print(dec_content)