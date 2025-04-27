def atbash_encrypt_decrypt(text):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            end = ord('z') if char.islower() else ord('Z')
            numerical_char = (ord(char) - base)
            en_char = chr(end - numerical_char)
            result += en_char
        elif char.isdigit():
            result += char
        else:
            result += char
    return result

file = input("Specify file path or name: ")

with open(file, 'r+', encoding="utf-8") as f:
    content = f.read()
    encrypt_message = atbash_encrypt_decrypt(content)
    f.seek(0)
    f.write(encrypt_message)
    f.truncate()