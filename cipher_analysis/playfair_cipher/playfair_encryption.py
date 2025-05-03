def create_playfair_grid(key):
    key = key.upper().replace('J','I')
    seen = set()
    grid = []

    for char in key:
        if char not in seen and char.isalpha():
            seen.add(char)
            grid.append(char)

    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char in alphabet:
        if char not in seen:
            grid.append(char)

    return [grid[i:i+5] for i in range(0, 25, 5)]

def find_position(char,grid):
    if char == 'J':
        char = 'I'

    for row in range(5):
        for col in range(5):
            if grid[row][col] == char:
                return row, col
    return None
        
def playfair_encryption(text, key):
    import re
    grid = create_playfair_grid(key)

    non_alpha = [(i, c) for i, c in enumerate(text) if not c.isalpha()]
    clean_text = ''.join([c for c in text.upper().replace('J', 'I') if c.isalpha()])

    digraphs = []
    i = 0
    while i < len(clean_text):
        a = clean_text[i]
        b = clean_text[i + 1] if i + 1 < len(clean_text) else 'X'
        if a == b:
            digraphs.append(a + 'X')
            i += 1
        else:
            digraphs.append(a + b)
            i += 2

    encrypted_text = ''
    for digraph in digraphs:
        first_char, second_char = digraph[0], digraph[1]
        row1, col1 = find_position(first_char, grid)
        row2, col2 = find_position(second_char, grid)

        if row1 == row2:
            encrypted_text += grid[row1][(col1 + 1) % 5]
            encrypted_text += grid[row2][(col2 + 1) % 5]
        elif col1 == col2:
            encrypted_text += grid[(row1 + 1) % 5][col1]
            encrypted_text += grid[(row2 + 1) % 5][col2]
        else:
            encrypted_text += grid[row1][col2]
            encrypted_text += grid[row2][col1]

    final_output = []
    encrypted_idx = 0

    for char in text:
        if char.isalpha():
            final_output.append(encrypted_text[encrypted_idx])
            encrypted_idx += 1
        else:
            final_output.append(char)

    return ''.join(final_output)


file = input("Specify file path or name: ")

key = input("Specify the key: ")

with open(file, 'r+', encoding="utf-8") as f:
    content = f.read()
    enc_content = playfair_encryption(content,key)
    f.seek(0)
    f.write(enc_content)
    f.truncate()