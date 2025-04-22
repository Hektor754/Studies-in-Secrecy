import matplotlib.pyplot as plt
import string
from collections import Counter

english_freq = {
    'A': 8.167, 'B': 1.492, 'C': 2.782, 'D': 4.253, 'E': 12.702,
    'F': 2.228, 'G': 2.015, 'H': 6.094, 'I': 6.966, 'J': 0.153,
    'K': 0.772, 'L': 4.025, 'M': 2.406, 'N': 6.749, 'O': 7.507,
    'P': 1.929, 'Q': 0.095, 'R': 5.987, 'S': 6.327, 'T': 9.056,
    'U': 2.758, 'V': 0.978, 'W': 2.360, 'X': 0.150, 'Y': 1.974, 'Z': 0.074
}


def frequency_comparison_visualization(english_freq,text):
    text = text.upper()
    filtered = [char for char in text if char.isalpha()]
    total = len(filtered)
    counts = Counter(filtered)
    cipher_freq = {char: round((count / total * 100), 2) for char, count in counts.items()}
    plt.figure(figsize=(12, 6))
    plt.bar(english_freq.keys(), english_freq.values(), alpha=0.5, label='English Frequency')
    plt.bar(cipher_freq.keys(), cipher_freq.values(), alpha=0.5, label='Ciphertext Frequency')
    plt.title('Letter Frequency Comparison')
    plt.xlabel('Letters')
    plt.ylabel('Frequency (%)')
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
    
file = input("Specify file path or name: ")
with open(file, "r") as f:
    cipher_text = f.read()
frequency_comparison_visualization(english_freq,cipher_text)
