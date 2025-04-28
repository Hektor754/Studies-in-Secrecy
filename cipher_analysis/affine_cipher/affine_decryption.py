def affine_encrypt(text):
    result = ""
    
    a_list = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    a_factor = int(input(f"choose a number for first key from these ones: {a_list}: "))
    b_factor = int(input("choose a number from 0 to 25 for the second key: "))

    while a_factor not in a_list or not (25 >= b_factor >= 0):
        a_factor = int(input(f"choose a number for first key from these ones: {a_list}: "))
        b_factor = int(input("choose a number from 0 to 25 for the second key: "))
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            letter_pos = (ord(char) - base)
            en_char = chr(((a_factor * letter_pos + b_factor) % 26) + base)
            result += en_char
        elif char.isdigit():
            result += char
        else:
            result += char
    return result


file = input("Specify file path or name: ")

with open(file, 'r+', encoding="utf-8") as f:
    content = f.read()
    encrypt_message = affine_encrypt(content)
    f.seek(0)
    f.write(encrypt_message)
    f.truncate()
