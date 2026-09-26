from cryptography.fernet import Fernet
import os

KEY_FILE = "secret.key"


# Generate or load encryption key
def load_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as file:
            return file.read()
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as file:
            file.write(key)
        return key


key = load_key()
cipher = Fernet(key)


# Encryption function
def encrypt_message():
    message = input("\nEnter the message to encrypt: ")

    encrypted = cipher.encrypt(message.encode())

    print("\nEncrypted Message:")
    print(encrypted.decode())


# Decryption function
def decrypt_message():
    encrypted_message = input("\nEnter the encrypted message: ")

    try:
        decrypted = cipher.decrypt(encrypted_message.encode())

        print("\nDecrypted Message:")
        print(decrypted.decode())

    except:
        print("\nInvalid encrypted message or key!")


# Main program
print("========================================")
print("   DATA ENCRYPTION AND DECRYPTION TOOL")
print("========================================")

while True:

    print("\n1. Encrypt Message")
    print("2. Decrypt Message")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        encrypt_message()

    elif choice == "2":
        decrypt_message()

    elif choice == "3":
        print("\nThank you for using the tool!")
        break

    else:
        print("\nInvalid choice. Please enter 1, 2 or 3.")
