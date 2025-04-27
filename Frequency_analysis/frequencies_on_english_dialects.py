import matplotlib.pyplot as plt

def monofrequency(text):
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    monofrequencies = {char: 0 for char in ALPHABET}
    text = ''.join([char.lower() for char in text if char.isalpha()])
    text = ''.join([char for char in text if char in ALPHABET])
    for char in text:
        monofrequencies[char] += 1
    total_chars = len(text)
    if total_chars > 0:
        for letter in monofrequencies:
            monofrequencies[letter] /= total_chars
    else:
        for letter in monofrequencies:
            monofrequencies[letter] = 0
    return monofrequencies

def plot_monofrequency(ax, text_freq, title, color):
    ax.bar(text_freq.keys(), text_freq.values(), alpha=0.7, label=title, color=color)
    ax.set_title(title)
    ax.set_xlabel('Letters')
    ax.set_ylabel('Frequency (%)')
    ax.legend()
    ax.grid(axis='y', linestyle='--', alpha=0.7)

def plot_frequency_differences(english_freq, american_freq, australian_freq, irish_freq):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    
    english_values = [english_freq[letter] for letter in letters]
    american_values = [american_freq[letter] for letter in letters]
    australian_values = [australian_freq[letter] for letter in letters]
    irish_values = [irish_freq[letter] for letter in letters]
    
    x = range(len(letters))
    
    width = 0.2
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar([i - 1.5 * width for i in x], english_values, width=width, label='English', color='skyblue')
    ax.bar([i - 0.5 * width for i in x], american_values, width=width, label='American', color='orange')
    ax.bar([i + 0.5 * width for i in x], australian_values, width=width, label='Australian', color='green')
    ax.bar([i + 1.5 * width for i in x], irish_values, width=width, label='Irish', color='red')
    
    ax.set_xticks(x)
    ax.set_xticklabels(letters)
    ax.set_title('Letter Frequency Differences Across Books')
    ax.set_xlabel('Letters')
    ax.set_ylabel('Frequency (%)')
    ax.legend()
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.tight_layout()

english_book = "Frequency_analysis/Dracula_by_Bram_Stoker.txt"
american_book = "Frequency_analysis/Short Story Classics (American) Vol. 2 by William Patten.txt"
irish_book = "Frequency_analysis/Dubliners by James Joyce.txt"
australian_book = "Frequency_analysis/Tales of the Bush by Henry Lawson.txt"

fig, axs = plt.subplots(2, 2, figsize=(12, 12))

with open(english_book, 'r', encoding="utf-8") as eng_f:
    eng_content = eng_f.read()
    eng_freq = monofrequency(eng_content)
    plot_monofrequency(axs[0, 0], eng_freq, 'English Frequency', 'skyblue')

with open(american_book, 'r', encoding="utf-8") as am_f:
    am_content = am_f.read()
    am_freq = monofrequency(am_content)
    plot_monofrequency(axs[0, 1], am_freq, 'American Frequency', 'orange')

with open(australian_book, 'r', encoding="utf-8") as au_f:
    au_content = au_f.read()
    au_freq = monofrequency(au_content)
    plot_monofrequency(axs[1, 0], au_freq, 'Australian Frequency', 'green')

with open(irish_book, 'r', encoding="utf-8") as ir_f:
    ir_content = ir_f.read()
    ir_freq = monofrequency(ir_content)
    plot_monofrequency(axs[1, 1], ir_freq, 'Irish Frequency', 'red')

plot_frequency_differences(eng_freq, am_freq, au_freq, ir_freq)

plt.tight_layout()
plt.show()