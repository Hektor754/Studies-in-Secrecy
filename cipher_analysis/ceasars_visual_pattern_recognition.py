import matplotlib.pyplot as plt
import string
from collections import Counter
import seaborn as sns

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

def calculate_index_of_coincidence(text):
    filtered = [char.upper() for char in text if char.isalpha()]
    N = len(filtered)

    if N <= 1:
        return 0

    counts = Counter(filtered)
    numerator = sum(f * (f - 1) for f in counts.values())
    denominator = N * (N - 1)

    return numerator / denominator

def visualize_ic_by_chunks(text, chunk_size=100):
    ics = []
    positions = []

    for i in range(0, len(text), chunk_size):
        chunk = text[i:i+chunk_size]
        ic = calculate_index_of_coincidence(chunk)
        ics.append(ic)
        positions.append(i)

    plt.figure(figsize=(12, 5))
    plt.plot(positions, ics, marker='o', linestyle='-', color='teal')
    plt.title("Index of Coincidence per Text Chunk")
    plt.xlabel("Starting Position in Ciphertext")
    plt.ylabel("Index of Coincidence")
    plt.grid(True)
    plt.axhline(y=0.065, color='green', linestyle='--', label="English IC (~0.065)")
    plt.axhline(y=0.038, color='red', linestyle='--', label="Random Text IC (~0.038)")
    plt.legend()
    plt.tight_layout()
    plt.show()

def bigram_trigram_visualizzation(text):
    text = text.upper()
    clean_text = ""
    heatmap = [[0 for _ in range(26)] for _ in range(26)]
    trigram_counts = Counter()
    for char in text:
        if char.isalpha():
            clean_text += char
    for i in range(len(clean_text) - 1):
        first = clean_text[i]
        second = clean_text[i + 1]
        row = ord(first) - ord('A')
        col = ord(second) - ord('A')
        heatmap[row][col] += 1
    for i in range(len(clean_text) - 2):
        first = clean_text[i]
        second = clean_text[i+1]
        third = clean_text[i+2]
        trigram = first + second + third
        trigram_counts[trigram] += 1
    most_common_trigrams = trigram_counts.most_common(10)


        
        
    plt.figure(figsize=(12, 10))
    sns.heatmap(heatmap, xticklabels=list(string.ascii_uppercase), yticklabels=list(string.ascii_uppercase), cmap="mako")
    plt.title("Bigram Frequency Heatmap")
    plt.xlabel("Second Letter")
    plt.ylabel("First Letter")
    plt.show()
    
    labels, values = zip(*most_common_trigrams)
    plt.figure(figsize=(10, 5))
    plt.bar(labels, values, color="teal")
    plt.title("Top 10 Trigrams")
    plt.xlabel("Trigram")
    plt.ylabel("Frequency")
    plt.show()

file = input("Specify file path or name: ")
with open(file, "r") as f:
    cipher_text = f.read()
frequency_comparison_visualization(english_freq,cipher_text)
visualize_ic_by_chunks(cipher_text, chunk_size=100)
bigram_trigram_visualizzation(cipher_text)
