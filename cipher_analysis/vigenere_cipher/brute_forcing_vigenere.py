from collections import Counter

common_words = ["the", "and", "that", "was", "with", "for"]

def check_for_common_words(decrypted_text):
    found_words = []
    for word in common_words:
        if word in decrypted_text.lower():
            found_words.append(word)
    return len(found_words)

def calculate_index_of_coincidence(text):
    filtered = [char.upper() for char in text if char.isalpha()]
    N = len(filtered)

    if N <= 1:
        return 0

    counts = Counter(filtered)
    numerator = sum(f * (f - 1) for f in counts.values())
    denominator = N * (N - 1)
    num = numerator / denominator

    return num

def decrypt(text, shift):
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
    return result

def calculate_letter_frequency(text):
    text = text.upper()
    filtered = [char for char in text if char.isalpha()]
    counts = Counter(filtered)
    total = sum(counts.values())
    freq = {letter: count / total for letter, count in counts.items()}
    return freq

def chi_squared_stat(cipher_freq, english_freq, total_letters):
    chi_squared = 0
    for letter in english_freq:
        expected = english_freq[letter] * total_letters
        observed = cipher_freq.get(letter, 0)
        chi_squared += ((observed - expected) ** 2) / expected
    return chi_squared

def brute_force_vigenere(text):
    english_freq = {
    'A': 0.082, 'B': 0.015, 'C': 0.028, 'D': 0.043, 'E': 0.13,
    'F': 0.022, 'G': 0.02, 'H': 0.061, 'I': 0.07, 'J': 0.0015,
    'K': 0.0077, 'L': 0.04, 'M': 0.024, 'N': 0.067, 'O': 0.075,
    'P': 0.019, 'Q': 0.00095, 'R': 0.06, 'S': 0.063, 'T': 0.091,
    'U': 0.028, 'V': 0.0098, 'W': 0.024, 'X': 0.0015, 'Y': 0.02, 'Z': 0.00074
    }

    answer = input("Do you know the key length? Press 1 for yes and 2 for no: ")
    english_val = 0.065
    groups = []
    list_of_averages = []

    if int(answer) == 1:
        key_length = int(input("Give key length: "))
        for i in range(key_length):
            group = ''.join([char for char in text[i::key_length] if char.isalpha()])
            groups.append(group)
    else:
        best_word_match_count = -1
        key_length = None
        for unknown_key in range(21,2):
            groups = []
            for i in range(unknown_key):
                group = ''.join([char for j, char in enumerate(text[i::unknown_key]) if char.isalpha()])
                groups.append(group)
                decrypted_group = ''.join([decrypt(group, shift) for shift in range(26)])      
                if check_for_common_words(decrypted_group) > 0:
                    key_length = unknown_key
                    break
            if key_length is not None:
                break

        print(f"Most probable key length: {key_length}")
    
    groups = [text[i::key_length] for i in range(key_length)]

    best_shift = None
    key_shifts = []

    for group in groups:
        best_shift = None
        best_score = float('inf')
        for shift in range(26):
            decrypted_group = decrypt(group, shift)
            frequency = calculate_letter_frequency(decrypted_group)
            score = chi_squared_stat(frequency, english_freq, len(group))

            if score < best_score:
                best_score = score
                best_shift = shift

        key_shifts.append(best_shift)
    
    print(f"Found key shifts: {key_shifts}")

    decrypted_text = ""
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = key_shifts[key_index % len(key_shifts)]
            base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - base - shift) % 26 + base)
            decrypted_text += shifted_char
            key_index += 1
        elif char.isdigit():
            shift = key_shifts[key_index % len(key_shifts)]
            shifted_num = str((int(char) - shift) % 10)
            decrypted_text += shifted_num
            key_index += 1
        else:
            decrypted_text += char

    print("\nDecrypted Text:")
    print(decrypted_text)

file = input("Specify file path or name: ")
                
with open(file, 'r') as f:
    content = f.read()
    decrypted = brute_force_vigenere(content)
        
        
