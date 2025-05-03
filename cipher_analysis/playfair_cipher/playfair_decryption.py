def create_playfair_square(phrase):
    """
    Generate the Playfair square for the given phrase.
    """
    key = key.replace('J', 'I').upper() + 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    key = "".join(dict.fromkeys(key))  # Remove duplicate letters
    grid = [[k for k in key[i:i+5]] for i in range(0, 25, 5)]
    return grid


def find_location(grid, char):
    """
    Helper function to get the row and column of the given char.
    """
    for i in range(0, 5):
        for j in range(0, 5):
            if grid[i][j] == char:
                return i, j

def playfair_decrypt(ciphertext: str, key: str) -> str:
    """
    Decrypt a message using the Playfair cipher.
    """
    playfair_square = create_playfair_square(key)
    message = ''

    # For each digraphs, substitute the characters using the grid
    for i in range(0, len(ciphertext), 2):
        digraph = ciphertext[i:i+2]
        row1, col1 = find_location(playfair_square, digraph[0])
        row2, col2 = find_location(playfair_square, digraph[1])
        if row1 == row2:
            sub1 = playfair_square[row1][(col1 - 1) % 5]
            sub2 = playfair_square[row2][(col2 - 1 ) % 5]
        elif col1 == col2:
            sub1 = playfair_square[(row1 - 1) % 5][col1]
            sub2 = playfair_square[(row2 - 1) % 5][col2]
        else:
            sub1 = playfair_square[row1][col2]
            sub2 = playfair_square[row2][col1]
        
        message += sub1 + sub2

    # Remove the 'X' between two similar letters
    i = 0
    while i < len(message) - 2:
        if message[i] == message[i+2] and message[i+1] == 'X':
            message = message[:i+1] + message[i+2:]
        i += 1

    # Remove the last 'X'
    if message[-1] == 'X':
        message = message[:-1]

    return message


file = input("Specify file path or name: ")
key = input("Specify the key: ")

with open(file, 'r+', encoding="utf-8") as f:
    content = f.read()
    dec_content = playfair_decrypt(content, key)
    f.seek(0)
    f.write(dec_content)
    f.truncate()

