def brute_force(text):
    for shift in range(1,26):
        result = ""
        for char in text:
            if char.isalpha():
                base = ord('a') if char.islower() else ord('A')
                shifted_char = chr((ord(char) - base - shift) % 26 + base)
                result += shifted_char
            elif char.isdigit():
                shifted_num = str((int(char) - shift) % 10)
                result += shifted_num
            else:
                result += char
        print(result)
        
file = "dknkfn.txt"

with open(file, 'r') as f:
    content = f.read()
    brute_force(content)