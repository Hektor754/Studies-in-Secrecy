# Vigenère Cipher

The Vigenère Cipher is a classic polyalphabetic substitution cipher that uses a keyword to shift letters in the plaintext by different amounts depending on the corresponding letter in the keyword.

## How It Works

Each letter of the message is encrypted by shifting it according to the corresponding letter in the **keyword**.  
For example, using the keyword **KEY**, you align each letter of the message with a repeating sequence of the keyword:

Plaintext: A T T A C K A T D A W N 

Keyword: K E Y K E Y K E Y K E Y


Each letter is then shifted by the alphabetical value of the keyword letter (e.g., **A = 0, B = 1, ..., Z = 25**).  
So with **K = 10**, **E = 4**, **Y = 24**, and so on.

This makes it more secure than the Caesar Cipher because it uses multiple shift values.

## Historical Background

The Vigenère Cipher was described in 1553 by Giovan Battista Bellaso but was later misattributed to Blaise de Vigenère.  
For centuries, it was considered unbreakable, earning the nickname “le chiffre indéchiffrable” (the indecipherable cipher), until it was eventually cracked in the 19th century.

## Files and Usage

This project contains the following files:

- `vigenere_cipher.py` — Encrypts a message using the Vigenère cipher.
- `vigenere_cipher_decrypt.py` — Decrypts an encrypted message using the provided keyword.
- `vigenere_brute_force.py` — Attempts to decrypt a message by brute-forcing potential keywords (basic/dictionary attack).
- `test_message_vigenere.txt` — A sample encrypted message for testing.

### Running the Program

1. **Decrypt the test message:**  
   Run `vigenere_cipher_decrypt.py` with the correct keyword on `test_message.txt` to get the decrypted text.

2. **Encrypt the test message:**  
   Use `vigenere_cipher.py` with your chosen keyword to encrypt the decrypted message again.

3. **Try brute forcing:**  
   Run `vigenere_brute_force.py` to attempt decryption by testing common keywords or small wordlists.

## Additional Notes

- Only alphabetic characters are encrypted; punctuation and whitespace are preserved.
- The keyword is case-insensitive but should only contain alphabetic characters.
- This cipher is more secure than Caesar but still vulnerable to cryptanalysis with enough ciphertext.
