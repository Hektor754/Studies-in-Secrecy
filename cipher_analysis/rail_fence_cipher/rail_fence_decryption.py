def rail_fence_decryption(cipher, num_rails):
    if num_rails <= 1:
        return cipher

    rail_pattern = [['' for _ in range(len(cipher))] for _ in range(num_rails)]
    
    direction = 1
    row = 0
    for col in range(len(cipher)):
        rail_pattern[row][col] = '*'
        if row == 0:
            direction = 1
        elif row == num_rails - 1:
            direction = -1
        row += direction

    idx = 0
    for r in range(num_rails):
        for c in range(len(cipher)):
            if rail_pattern[r][c] == '*' and idx < len(cipher):
                rail_pattern[r][c] = cipher[idx]
                idx += 1

    result = ""
    row = 0
    direction = 1
    for col in range(len(cipher)):
        result += rail_pattern[row][col]
        if row == 0:
            direction = 1
        elif row == num_rails - 1:
            direction = -1
        row += direction

    return result

file = input("Specify file path or name: ")
rail_choice = int(input("pick how many rails you want: "))

with open(file, 'r+', encoding="utf-8") as f:
    content = f.read()
    encrypt_message = rail_fence_decryption(content,rail_choice)
    f.seek(0)
    f.write(encrypt_message)
    f.truncate()
