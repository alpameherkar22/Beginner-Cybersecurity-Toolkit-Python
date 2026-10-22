import os

def encrypt_decrypt_file(file_path, key, output_path):
    """Encrypts or decrypts a file using a repeating key XOR cipher."""
    if not os.path.exists(file_path):
        print(f"[ERROR] File '{file_path}' not found.")
        return

    try:
        # reading file in binary mode
        with open(file_path, "rb") as f:
            data = f.read()

        key_bytes = key.encode('utf-8')
        output_data = bytearray()

        # applying XOR cipher byte-by-byte with the repeating key
        for i in range(len(data)):
            encrypt_byte = data[i] ^ key_bytes[i % len(key_bytes)]
            output_data.append(encrypt_byte)

        # writing transformed bytes into output file
        with open(output_path, "wb") as f:
            f.write(output_data)

        print(f"[SUCCESS] Operation Completed! Saved as: {output_path}")

    except Exception as e:
        print(f"[ERROR] An error occurred: {e}")

if __name__ == "__main__":
    print("--- CUSTOM FILE ENCRYPTOR / DECRYPTOR ---")
    choice = input("Do you want to (1) Encrypt or (2) Decrypt? Enter 1 or 2: \n>")
    target_file = input("Enter the filename (e.g. sensitive.txt): \n>")
    secret_key = input("Enter your secret key phrase: \n>")

    if choice == "1":
        output_file = target_file + ".enc"
        encrypt_decrypt_file(target_file, secret_key, output_file)

    elif choice == "2":
        # removing .enc or creating a decrypted output file
        output_file = target_file.replace(".enc", "_decrypted.txt")
        encrypt_decrypt_file(target_file, secret_key, output_file)

    else:
        print("[ERROR] Invalid Choice. Please run the script again.") 