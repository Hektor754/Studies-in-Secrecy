import hashlib

def sha256_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

def dictionary_attack(hash_to_crack, wordlist_path):
    with open(wordlist_path, 'r') as f:
        for word in f:
            word = word.strip()
            if sha256_hash(word) == hash_to_crack:
                return f"Password found: {word}"
    return 'Password not found in the dictionary'

wordlist = input("Specify the wordlist path: ")
password_file = input("Give the file path containing the password: ")

with open(password_file, 'r') as f:
    password = f.read().strip()

hashed_password = sha256_hash(password)

result = dictionary_attack(hashed_password, wordlist)
print(result)

