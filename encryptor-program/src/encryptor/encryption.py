def choose_encryption_type():
    # Function to choose the type of encryption
    encryption_types = ['AES', 'DES', 'RSA']
    print("Choose an encryption type:")
    for i, et in enumerate(encryption_types, start=1):
        print(f"{i}. {et}")
    choice = int(input("Enter the number of your choice: "))
    return encryption_types[choice - 1]

def encrypt_string(string_to_encrypt, encryption_type):
    # Function to encrypt a string based on the chosen encryption type
    from cryptography.fernet import Fernet
    import base64
    import os

    if encryption_type == 'AES':
        key = Fernet.generate_key()
        cipher = Fernet(key)
        encrypted_string = cipher.encrypt(string_to_encrypt.encode())
        return base64.urlsafe_b64encode(key).decode(), encrypted_string.decode()
    elif encryption_type == 'DES':
        # Placeholder for DES encryption logic
        pass
    elif encryption_type == 'RSA':
        # Placeholder for RSA encryption logic
        pass
    else:
        raise ValueError("Invalid encryption type selected.")

def main():
    string_to_encrypt = input("Enter the string to encrypt: ")
    encryption_type = choose_encryption_type()
    alias = input("Enter an alias for this record: ")
    
    key, encrypted_string = encrypt_string(string_to_encrypt, encryption_type)
    
    print(f"Alias: {alias}")
    print(f"Encrypted String: {encrypted_string}")
    print(f"Decryption Key: {key}")

if __name__ == "__main__":
    main()