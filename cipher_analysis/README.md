# 🔐 Cipher Analysis

This project explores the creation and analysis of simple ciphers—both classical and modern—in code. Its purpose is to help you understand how basic encryption techniques work, what encrypted messages look like, and how to decrypt or crack them using various methods.

Whether you're interested in cryptography, programming, or cybersecurity, this repository provides a hands-on introduction to the building blocks of encryption and decryption.

---

## 📁 Project Structure

The repository is organized into multiple folders, each corresponding to a specific cipher.  
Currently, there are **8 ciphers** implemented, and each folder typically contains the following files:

- `encrypt.py` – Demonstrates how the cipher encrypts plaintext.
- `decrypt.py` – Reverses the encryption to retrieve the original message.
- `brute_force.py` – (If applicable) Attempts to crack the cipher without knowing the key.

Some folders may also include:
- `output.txt` – A saved file containing the results of a brute-force attack, especially when the output is large.

---

## 🔒 Encryption

Each encryption script shows how a plaintext message is transformed into ciphertext. This might involve:

- Substituting letters or characters
- Shifting letters (e.g., Caesar Cipher)
- Using a keyword to alter encryption (e.g., Vigenère Cipher)
- Performing binary operations (e.g., XOR Cipher)

These examples demonstrate the fundamental ideas behind how data is secured.

---

## 🔓 Decryption

Decryption scripts are designed to reverse the encryption process and retrieve the original message.  
This illustrates the essence of cryptography: securing information in transit, but also ensuring it's readable at the final destination.

---

## 🛠️ Brute Force

Brute force is a method used to crack encrypted messages when the key is unknown. It works by:

1. Trying every possible key or configuration allowed by the cipher.
2. Checking the output for a valid or readable message.

If a brute-force script generates too many possible outputs, a file (like `output.txt`) may be included to store the results.

---

Feel free to explore each cipher folder, study the logic, modify the code, or contribute your own ciphers to the project!