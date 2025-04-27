def vigenere_encrypt(text, key):
    result = ""
    key = key.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[key_index % len(key)]) - ord('A')
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            result += shifted_char
            key_index += 1

        elif char.isdigit():
            shift = ord(key[key_index % len(key)]) - ord('A')
            shifted_num = str((int(char) + shift) % 10)
            result += shifted_num
            key_index += 1

        else:
            result += char

    return result


file = input("Specify file path or name: ")

key = input("Specify the key: ")

with open(file, 'r+', encoding="utf-8") as f:
    content = f.read()
    enc_content = vigenere_encrypt(content,key)
    f.seek(0)
    f.write(enc_content)
    f.truncate()

