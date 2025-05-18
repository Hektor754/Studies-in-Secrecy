# Caesar Cipher

The Caesar Cipher is a classic substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

## How It Works

Each letter of the message is converted to its corresponding numerical value  
(for example, **a = 1, b = 2, ..., z = 26**). Then, the letter's numerical value is shifted by a specified amount (called the **shift**).  
For example, with a shift of 3, **a** becomes **d**, **b** becomes **e**, and so on.

Unlike the original cipher, which used a fixed shift of 3, this implementation allows you to choose any shift value.

## Historical Background

The cipher is named after Julius Caesar, who reportedly used this technique to encrypt messages of military importance. While Caesar's use is the earliest recorded, substitution ciphers predate his time.

## Files and Usage

This project contains the following files:

- `ceasars_cipher.py` — Encrypts a message using the Caesar cipher.
- `ceasars_cipher_decrypt.py` — Decrypts an encrypted message.
- `brute_forcing_ceasar.py` — Attempts to decrypt a message by trying all possible shifts.
- `ceasars_frequency_analysis.py` — Uses frequency analysis to help decrypt a message.
- `test_message.txt` — A sample encrypted message for testing.

### Running the Program

1. **Decrypt the test message:**  
   Run `ceasars_cipher_decrypt.py` on `test_message.txt` to get the decrypted text.

2. **Encrypt the test message:**  
   Use `ceasars_cipher.py` with your chosen shift to encrypt the decrypted message again.

3. **Try brute forcing:**  
   Run `brute_forcing_ceasar.py` to attempt all shifts and see which produces a readable message.

4. **Frequency analysis:**  
   Use `ceasars_frequency_analysis.py` to decrypt messages by analyzing letter frequency.

## Additional Notes

- The cipher works only with letters; punctuation and whitespace are generally ignored or preserved as is.
- The alphabet is considered cyclic (after `z` comes `a` again).
- This implementation assumes lowercase input but can be adapted for uppercase.
