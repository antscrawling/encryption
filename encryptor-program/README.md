# Encryptor Program

## Overview
The Encryptor Program is a Python application designed to securely encrypt and manage sensitive strings. It allows users to create profiles, encrypt strings, and manage their data while ensuring that only authorized users can access certain functionalities.

## Features
- User profile creation and management
- String encryption and decryption
- Multiple encryption algorithms
- User activity logging
- Admin functionalities for user management

## Project Structure
```
encryptor-program
├── src
│   ├── main.py                # Entry point of the application
│   ├── encryptor              # Contains encryption and decryption logic
│   │   ├── __init__.py
│   │   ├── encryption.py       # Functions for encrypting strings
│   │   └── decryption.py       # Functions for decrypting strings
│   ├── database                # Database models and setup
│   │   ├── __init__.py
│   │   ├── models.py           # SQLAlchemy models for User and Encrypted String tables
│   │   └── db_setup.py         # Database setup functions
│   ├── user                    # User management functionalities
│   │   ├── __init__.py
│   │   ├── user_management.py   # Functions for managing user profiles
│   │   └── user_profile.py      # User profile-related operations
│   ├── utils                   # Utility functions
│   │   ├── __init__.py
│   │   ├── logger.py           # Logging user activities
│   │   └── clipboard.py        # Functions for clipboard operations
├── requirements.txt            # Project dependencies
├── README.md                   # Project documentation
└── .gitignore                  # Files to ignore in version control
```

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/antscrawling/encryptor-program.git
   ```
2. Navigate to the project directory:
   ```
   cd encryptor-program
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run the application:
   ```
   python src/main.py
   ```
2. Follow the on-screen instructions to create a user profile, encrypt strings, and manage your data.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.