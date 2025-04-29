def affine_brute_force(text):
    a_list = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    count = 1

    with open("affine_brute_output.txt", "w", encoding="utf-8") as out:
        for a_value in a_list:
            inverse_a = pow(a_value, -1, 26)
            for b_value in range(26):
                result = ""
                for char in text:
                    if char.isalpha():
                        base = ord('a') if char.islower() else ord('A')
                        en_char = ord(char) - base
                        dec_char = chr(((inverse_a * (en_char - b_value)) % 26) + base)
                        result += dec_char
                    elif char.isdigit():
                        result += char
                    else:
                        result += char
                out.write(f"{count}. Key pair: [{a_value},{b_value}]\n")
                out.write("-" * 30 + "\n")
                out.write(result + "\n")
                out.write("-" * 30 + "\n\n")
                count += 1

file = input("Specify file path or name: ")

with open(file, 'r', encoding="utf-8") as f:
    content = f.read()
    affine_brute_force(content)