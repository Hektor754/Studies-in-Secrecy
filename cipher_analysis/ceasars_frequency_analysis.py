from collections import Counter

english_freq = {
    'E': 12.7, 'T': 9.1, 'A': 8.2, 'O': 7.5, 'I': 7.0,
    'N': 6.7, 'S': 6.3, 'H': 6.1, 'R': 6.0, 'D': 4.3,
    'L': 4.0, 'C': 2.8, 'U': 2.8, 'M': 2.4, 'W': 2.4,
    'F': 2.2, 'G': 2.0, 'Y': 2.0, 'P': 1.9, 'B': 1.5,
    'V': 1.0, 'K': 0.8, 'J': 0.15, 'X': 0.15, 'Q': 0.1, 'Z': 0.07
}

def get_cipher_frequency(text):
    text = text.upper()
    filtered = [char for char in text if char.isalpha()]
    total = len(filtered)
    counts = Counter(filtered)
    freq = {char: round((count / total * 100), 2) for char, count in counts.items()}
    return freq

def apply_mapping(text, mapping):
    result = ""
    for char in text:
        if char.upper() in mapping:
            mapped_char = mapping[char.upper()]
            result += mapped_char.lower() if char.islower() else mapped_char
        else:
            result += char
    return result

def generate_alternate_mappings(cipher_sorted, english_sorted, top_n=5):
    mappings = []
    for shift in range(top_n):
        mapping = {}
        for i in range(len(cipher_sorted)):
            if i + shift < len(english_sorted):
                mapping[cipher_sorted[i][0]] = english_sorted[i + shift][0]
        mappings.append(mapping)
    return mappings

def generate_swap_mappings(cipher_sorted, english_sorted, max_swaps=3):
    mappings = []
    for swap_pos in range(max_swaps):
        cipher_copy = cipher_sorted.copy()
        if swap_pos > 0:
            cipher_copy[0], cipher_copy[swap_pos] = cipher_copy[swap_pos], cipher_copy[0]
        mapping = {}
        for (c_letter, _), (e_letter, _) in zip(cipher_copy, english_sorted):
            mapping[c_letter] = e_letter
        mappings.append(mapping)
    return mappings

file = input("Specify file path or name: ")
with open(file, "r") as f:
    cipher_text = f.read()

cipher_freq = get_cipher_frequency(cipher_text)
cipher_freq_sorted = sorted(cipher_freq.items(), key=lambda x: x[1], reverse=True)
english_freq_sorted = sorted(english_freq.items(), key=lambda x: x[1], reverse=True)

alt_mappings = generate_alternate_mappings(cipher_freq_sorted, english_freq_sorted, top_n=3)
swap_mappings = generate_swap_mappings(cipher_freq_sorted, english_freq_sorted, max_swaps=3)
all_mappings = alt_mappings + swap_mappings

print("\n=======================")
print("🔍 Cipher Frequencies:")
print("=======================")
for letter, freq in cipher_freq.items():
    print(f"{letter}: {freq}%")

for i, mapping in enumerate(all_mappings):
    guessed_text = apply_mapping(cipher_text, mapping)
    print(f"\n=========================")
    print(f"🔁 Attempt {i+1}:")
    print("=========================")
    print("🗺️ Mapping:", mapping)
    print("\n🔓 Decryption Preview:\n")
    print(guessed_text[:300]) 

final_mapping = all_mappings[0]
final_text = apply_mapping(cipher_text, final_mapping)

print("\n=======================")
print("✅ Final Guess Output:")
print("=======================")
print("\n🗺️ Mapping Used:", final_mapping)
print("\n🔓 Full Decryption:\n")
print(final_text)

output_file = "half_baked_decryption.txt"
with open(output_file, "w") as out:
    out.write(final_text)  