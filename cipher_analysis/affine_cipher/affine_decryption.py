def affine_decryption(text):
    result = ""
    
    a_list = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    a_factor = int(input(f"first key: {a_list}: "))
    b_factor = int(input("the second key from 0 to 25: "))

    while a_factor not in a_list or not (25 >= b_factor >= 0):
        a_factor = int(input(f"first key: {a_list}: "))
        b_factor = int(input("the second key from 0 to 25: "))
    
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            en_char = ord(char) - base
            inverse_a = pow(a_factor, -1, 26)
            dec_char = chr(((inverse_a * (en_char - b_factor)) % 26) + base)
            result += dec_char
        elif char.isdigit():
            result += char
        else:
            result += char
    return result

file = input("Specify file path or name: ")

with open(file, 'r+', encoding="utf-8") as f:
    content = f.read()
    decrypt_message = affine_decryption(content)
    f.seek(0)
    f.write(decrypt_message)
    f.truncate()