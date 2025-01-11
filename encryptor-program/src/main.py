# main.py

from database.db_setup import setup_database
from user.user_management import create_user, delete_user, reset_password
from user.user_profile import view_user_profile, deactivate_user
from encryptor.encryption import encrypt_string, choose_encryption_type
from encryptor.decryption import decrypt_string, get_decryption_code
from utils.logger import log_activity
from utils.clipboard import copy_to_clipboard
from datetime import datetime
from database.db_setup import save_encrypted_string





def main():
    # Initialize the application
    setup_database()
    
    while True:
        print("Welcome to the Encryptor Program")
        print("1. Create User Profile")
        print("2. Delete User Profile")
        print("3. Encrypt String")
        print("4. View User Profile")
        print("5. Deactivate Profile")
        print("6. Reset Password")
        print("7. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            # input data from below fields
            #username, password, first_name, last_name, user_type, secret_question, secret_answer, email, phone):
            
            global username 
            username = input("Enter username: ")
            password = input("Enter password: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            user_type = input("Enter user type: ")
            secret_question = input("Enter secret question: ")
            secret_answer = input("Enter secret answer: ")
            email = input("Enter email: ")
            phone = input("Enter phone number: ")

            create_user(username, password, first_name, last_name, user_type, secret_question, secret_answer, email, phone)
            log_activity(user=username,activity=f"Created new user profile with username: {username}")
        elif choice == '2':
            delete_user()
        elif choice == '3':
            #username = 'antscrawling'
            
            string_to_encrypt = input("Enter string to encrypt: ")
            alias = input("Enter alias for this record: ")
            encryption_type = choose_encryption_type()
            encrypted_string, decryption_code = encrypt_string(string_to_encrypt, encryption_type)
            copy_to_clipboard(encrypted_string)
            log_activity( user=username,activity=f"Encrypted string with alias: {alias}, string: {string_to_encrypt}")
            #save to database
            save_encrypted_string(alias, encrypted_string, decryption_code, encryption_type, datetime.today().date(), 'antscrawling')
 
 
            
        elif choice == '4':
            view_user_profile()
            log_activity(user=username,activity=f"Viewed own profile {username}")
        elif choice == '5':
            deactivate_user()
        elif choice == '6':
            reset_password()
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()