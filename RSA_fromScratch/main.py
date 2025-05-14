from key_gen import generate_rsa_keys, rsa_encryption, rsa_decryption, load_key_from_pem

def main():
    print("1. Generate RSA Keys")
    print("2. Encrypt a Message")
    print("3. Decrypt a Message")
    
    choice = input("Press the corresponding number: ")

    while choice not in ["1", "2", "3"]:
        print("Invalid input. Try again...\n")
        print("==========================\n")
        
        print("1. Generate RSA Keys")
        print("2. Encrypt a Message")
        print("3. Decrypt a Message")
        choice = input("Press the corresponding number: ")

    if choice == "1":
        generate_rsa_keys()
        print("Keys generated and saved")
    
    elif choice == "2":
        n, e = load_key_from_pem("public_key.pem")
        file = input("Provide the File Path: ")
        with open(file, 'r') as f:
            message = f.read()
        
        ciphertext = rsa_encryption(message, e, n)
        
        encrypted_file = file + "_encrypted.txt"
        with open(encrypted_file, 'w') as f:
            f.write(str(ciphertext))
        
        print(f"Message encrypted and saved to {encrypted_file}")
    
    elif choice == "3":
        n, d = load_key_from_pem("private_key.pem")
        d_file = input("Provide the Encrypted File Path: ")
        with open(d_file, 'r') as en_f:
            ciphertext = int(en_f.read())
        
        plaintext = rsa_decryption(ciphertext, n, d)
        
        decrypted_file = d_file.replace("_encrypted.txt", "_decrypted.txt")
        with open(decrypted_file, 'w') as f:
            f.write(plaintext)
        
        print(f"Message decrypted and saved to {decrypted_file}")

if __name__ == "__main__":
    main()