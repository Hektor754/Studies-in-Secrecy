def rail_fence_encryption(text,num_rails):
    if num_rails <= 1:
        return text
    
    rails = ['' for _ in range(num_rails)]
    current_rail = 0
    direction = 1

    for char in text:
        rails[current_rail] += char

        if current_rail == 0:
            direction = 1
        elif current_rail == num_rails - 1:
            direction = -1

        current_rail += direction

    return ''.join(rails)

file = input("Specify file path or name: ")
rail_choice = int(input("pick how many rails you want: "))

with open(file, 'r+', encoding="utf-8") as f:
    content = f.read()
    encrypt_message = rail_fence_encryption(content,rail_choice)
    f.seek(0)
    f.write(encrypt_message)
    f.truncate()
    
