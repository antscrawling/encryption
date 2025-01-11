from cryptography.fernet import Fernet
import base64
from database.db_setup import setup_database, EncryptedString

def decrypt_string(encrypted_string, decryption_code):
    cipher = Fernet(base64.urlsafe_b64decode(decryption_code))
    decrypted_string = cipher.decrypt(encrypted_string.encode()).decode()
    return decrypted_string

def get_decryption_code(alias):
    session = setup_database()
    encrypted_string_record = session.query(EncryptedString).filter_by(alias=alias).first()
    session.close()
    if encrypted_string_record:
        return encrypted_string_record.decryption_code
    return None
