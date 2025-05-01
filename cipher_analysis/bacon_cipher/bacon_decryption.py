def bacon_steganography_decryption(text):
    result = ""
    bits = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rev_bacon_map = {format(i, '05b'): char for i, char in enumerate(alphabet)}

    for char in text:
        if char.isalpha():
            bits += '0' if char.islower() else '1'
            if len(bits) == 5:
                decoded_char = rev_bacon_map.get(bits, '?')
                result += decoded_char
                bits = ""
        else:
            result += char

    return result

def bacon_decryption(text):
    result = ""
    bits = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rev_bacon_map = {format(i, '05b'): char for i, char in enumerate(alphabet)}

    for char in text:
        if char.isalpha():
            bits += '0' if char == 'A' else '1'
            if len(bits) == 5:
                decoded_char = rev_bacon_map.get(bits, '?')
                result += decoded_char
                bits = ""
        else:
            result += char
    
    return result

choice = int(input("Choose 1. for traditional bacon cipher or 2. for steganography form bacon cipher: "))
if choice == 1:
    file = input("Specify file path or name: ")

    with open(file, 'r+', encoding="utf-8") as f:
        content = f.read()
        encrypt_message = bacon_decryption(content)
        f.seek(0)
        f.write(encrypt_message)
        f.truncate()
else:
    file = input("Specify file path or name: ")

    with open(file, 'r+', encoding="utf-8") as f:
        content = f.read()
        encrypt_message = bacon_steganography_decryption(content)
        f.seek(0)
        f.write(encrypt_message)
        f.truncate()