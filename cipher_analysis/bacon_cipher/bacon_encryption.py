import random
import string

def bacon_encryption(text):
    result = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    bacon_map = {char: format(i, '05b') for i, char in enumerate(alphabet)}
    all_letters = string.ascii_letters
    for char in text:
        if char.isalpha():
            binary_letter = bacon_map[char.upper()]
            en_char = binary_letter.replace('0', 'A').replace('1', 'B')
            result += en_char
        elif char.isdigit():
            result += char
        else:
            result += char
    return result

def bacon_steganography_encryption(text):
    result = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    bacon_map = {char: format(i, '05b') for i, char in enumerate(alphabet)}
    all_letters = string.ascii_letters
    for char in text:
        if char.isalpha():
            binary_letter = bacon_map[char.upper()]
            random_sequence = ''.join(random.sample(all_letters, 5))
            en_char = ''.join(char.lower() if b == '0' else char.upper() for b,char in zip(binary_letter,random_sequence))
            result += en_char
        elif char.isdigit():
            result += char
        else:
            result += char
    return result

choice = int(input("Choose 1. for traditional bacon cipher or 2. for steganography form bacon cipher: "))
if choice == 1:
    file = input("Specify file path or name: ")

    with open(file, 'r+', encoding="utf-8") as f:
        content = f.read()
        encrypt_message = bacon_encryption(content)
        f.seek(0)
        f.write(encrypt_message)
        f.truncate()
else:
    file = input("Specify file path or name: ")

    with open(file, 'r+', encoding="utf-8") as f:
        content = f.read()
        encrypt_message = bacon_steganography_encryption(content)
        f.seek(0)
        f.write(encrypt_message)
        f.truncate()

