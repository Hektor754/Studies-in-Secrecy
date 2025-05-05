import numpy as np

def mod_inverse(a,m):
    for x in range(1,m):
        if (a*x) % m == 1:
            return x
    return -1

def matrix_inverse(matrix):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = mod_inverse(det, 26)

    if det_inv == -1:
        raise ValueError("Matrix is not invertible. Cannot decrypt")
    
    adjugate = np.round(np.linalg.inv(matrix) * np.linalg.det(matrix)).astype(int) % 26
    inverse_matrix = (det_inv * adjugate) % 26
    return inverse_matrix

def hill_encryption(text,key):
    result = ""
    chunks = []
    pos = []
    decrypted_chunk_list = []

    text,pos = excluded_positions(text)
    text = text.upper()
    base = ord('A')

    if len(key) == 4:
        key_matrix = np.array([[ord(char) - base for char in key[:2]], 
                               [ord(char) - base for char in key[2:4]]])
        
        key_inv_matrix = matrix_inverse(key_matrix)

        chunks =[text[i:i+2] for i in range(0, len(text), 2)]

        for value in chunks:
            if len(value) < 2:
                value += 'X'
            letter_matrix = np.array([[ord(value[0]) - base],
                                      [ord(value[1]) - base]])
            
            decrypted_chunk = np.dot(key_inv_matrix, letter_matrix) % 26
            decrypted_chunk_list.append(decrypted_chunk)
    else:
        key_matrix = np.array([[ord(char) for char in key[:3]], 
                               [ord(char) for char in key[3:6]], 
                               [ord(char) for char in key[6:9]]])
        
        key_inv_matrix = matrix_inverse(key_matrix)

        chunks = [text[i:i+3] for i in range(0, len(text), 3)]

        for value in chunks:
            if len(value) < 3:
                value += 'X'
            letter_matrix = np.array([[ord(value[0]) - base],
                                      [ord(value[1]) - base],
                                      [ord(value[2]) - base]])
            
            decrypted_chunk = np.dot(key_inv_matrix,letter_matrix) % 26
            decrypted_chunk_list.append(decrypted_chunk)

    for chunk in decrypted_chunk_list:
        for num in chunk:
            result += chr(int(num[0]) + base)

    result_list = list(result)
    
    for index,char in pos:
        result_list.insert(index,char)

    return ''.join(result_list)

def excluded_positions(text):
    excluded = []
    clean_message = ""

    for index, char in enumerate(text):
        if char.isalpha():
            clean_message += char
        else:
            excluded.append((index, char))
    
    return clean_message, excluded

file = input("Specify file path or name: ")

key = input("Provide a key 4 letters long or 9 letters long: ")

while (len(key) != 4 and len(key) != 9) or (key.isalpha() == False):
    print("Incorrect key length or data type try again: ")
    print("===========================\n")
    key = input("Provide a key 4 letters long or 9 letters long: ")

with open(file, 'r+', encoding="utf-8") as f:
    content = f.read()
    enc_content = hill_encryption(content,key)
    f.seek(0)
    f.write(enc_content)
    f.truncate()