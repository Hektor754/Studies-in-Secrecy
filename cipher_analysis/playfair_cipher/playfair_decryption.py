def create_playfair_square(key):
    key = key.replace('J', 'I').upper() + 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    key = "".join(dict.fromkeys(key))
    grid = [[k for k in key[i:i+5]] for i in range(0, 25, 5)]
    return grid

def find_location(grid, char):
    for i in range(5):
        for j in range(5):
            if grid[i][j] == char:
                return i, j

def playfair_decrypt(text, key):
    playfair_square = create_playfair_square(key)

    clean_text = ''.join([c for c in text.upper().replace('J', 'I') if c.isalpha()])
    decrypted = ''

    for i in range(0, len(clean_text), 2):
        digraph = clean_text[i:i+2]
        if len(digraph) < 2:
            continue
        row1, col1 = find_location(playfair_square, digraph[0])
        row2, col2 = find_location(playfair_square, digraph[1])
        if row1 == row2:
            decrypted += playfair_square[row1][(col1 - 1) % 5]
            decrypted += playfair_square[row2][(col2 - 1) % 5]
        elif col1 == col2:
            decrypted += playfair_square[(row1 - 1) % 5][col1]
            decrypted += playfair_square[(row2 - 1) % 5][col2]
        else:
            decrypted += playfair_square[row1][col2]
            decrypted += playfair_square[row2][col1]

    i = 0
    clean_decrypted = ''
    while i < len(decrypted):
        if i + 2 < len(decrypted) and decrypted[i] == decrypted[i+2] and decrypted[i+1] == 'X':
            clean_decrypted += decrypted[i]
            i += 2
        else:
            clean_decrypted += decrypted[i]
            i += 1
    if len(clean_text) % 2 == 1 and clean_decrypted.endswith('X'):
        clean_decrypted = clean_decrypted[:-1]

    final_output = []
    alpha_index = 0
    for char in text:
        if char.isalpha():
            if alpha_index < len(clean_decrypted):
                final_output.append(clean_decrypted[alpha_index])
                alpha_index += 1
            else:
                final_output.append(char)
        else:
            final_output.append(char)

    return ''.join(final_output)

file = input("Specify file path or name: ")
key = input("Specify the key: ")

with open(file, 'r+', encoding="utf-8") as f:
    content = f.read()
    dec_content = playfair_decrypt(content, key)
    f.seek(0)
    f.write(dec_content)
    f.truncate()