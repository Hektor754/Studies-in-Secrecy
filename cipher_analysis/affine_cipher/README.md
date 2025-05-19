# Affine Cipher

The Affine Cipher is a type of monoalphabetic substitution cipher based on simple mathematical functions. It uses two keys, **a** and **b**, to encrypt and decrypt messages through modular arithmetic.

## How It Works

The encryption function for a single letter is:

E(x) = (a * x + b) mod m

- **x** is the letter's position in the alphabet (e.g., a = 0, b = 1, ..., z = 25)
- **a** and **b** are keys chosen such that **a** and **m** (alphabet size, usually 26) are coprime
- **m** is the size of the alphabet (26 for English)

The decryption function is:

D(x) = a_inv * (x - b) mod m


Where **a_inv** is the modular multiplicative inverse of **a** modulo **m**.

> **Important:** The key **a** must be coprime with 26 (i.e., gcd(a, 26) == 1) to ensure that the cipher is reversible.

## Historical Background

The Affine Cipher is a special case of the more general class of substitution ciphers. It improves on the Caesar Cipher by introducing multiplication into the transformation, making cryptanalysis slightly more difficult, though still easily breakable with modern tools.

## Files and Usage

This project contains the following files:

- `affine_cipher.py` — Encrypts a message using the Affine cipher.
- `affine_cipher_decrypt.py` — Decrypts an Affine-encrypted message using the correct keys.
- `affine_brute_force.py` — Attempts to decrypt a message by testing all valid key pairs (where **a** is coprime with 26).
- `test_message.txt` — A sample encrypted message for testing.

### Running the Program

1. **Decrypt the test message:**  
   Run `affine_cipher_decrypt.py` with the correct **a** and **b** values on `test_message.txt`.

2. **Encrypt the test message:**  
   Use `affine_cipher.py` with your chosen valid keys to encrypt the decrypted message again.

3. **Try brute forcing:**  
   Run `affine_brute_force.py` to attempt decryption by trying all key pairs (with valid **a** values).

## Additional Notes

- Only alphabetic characters are encrypted; punctuation and spaces are usually preserved.
- The alphabet is assumed to be lowercase English letters.
- Ensure that **a** and 26 are coprime to avoid runtime errors or irreversible encryption.