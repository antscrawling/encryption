from sqlalchemy.orm import sessionmaker
from database.db_setup import create_engine, User, EncryptedString
from utils.clipboard import copy_to_clipboard
from utils.logger import log_activity

def create_user(username, password, first_name, last_name, user_type, secret_question, secret_answer, email, phone):
    # Logic to create a new user profile in the database
    
    # For demonstration purposes, we will just print the user data
    print("New user profile created:")
    
    
def delete_user(username):
    engine = create_engine("sqlite:///encryptor.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    user = session.query(User).filter_by(username=username).first()
    if user:
        session.delete(user)
        session.commit()
        log_activity(user=username, activity=f"Deleted user profile with username: {username}")
        session.close()
        return True
    session.close()
    return False

def reset_password(username, secret_question, secret_answer, new_password):
    engine = create_engine("sqlite:///encryptor.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    user = session.query(User).filter_by(username=username, secret_question=secret_question, secret_answer=secret_answer).first()
    if user:
        user.password = new_password
        session.commit()
        log_activity(user=username, activity=f"Reset password for user: {username}")
        session.close()
        return True
    session.close()
    return False

def deactivate_user(username):
    engine = create_engine("sqlite:///encryptor.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    user = session.query(User).filter_by(username=username).first()
    if user:
        user.active_status = False
        session.commit()
        log_activity(user=username, activity=f"Deactivated user profile with username: {username}")
        session.close()
        return True
    session.close()
    return False

def view_user_data(username):
    engine = create_engine("sqlite:///encryptor.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    user = session.query(User).filter_by(username=username).first()
    session.close()
    if user:
        return {
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "phone": user.phone,
            "active_status": user.active_status,
            "alias": user.alias
        }
    return None

def list_user_aliases(username):
    engine = create_engine("sqlite:///encryptor.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    user = session.query(User).filter_by(username=username).first()
    session.close()
    if user and user.alias:
        return user.alias.split(',')
    return []

def copy_encrypted_string_and_key(alias):
    engine = create_engine("sqlite:///encryptor.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    encrypted_string_record = session.query(EncryptedString).filter_by(alias=alias).first()
    session.close()
    if encrypted_string_record:
        copy_to_clipboard(f"Encrypted String: {encrypted_string_record.encrypted_string}, Decryption Key: {encrypted_string_record.decryption_code}")
        log_activity(user=encrypted_string_record.username, activity=f"Copied encrypted string and key for alias: {alias}")
        return True
    return False

def delete_encrypted_string(alias):
    engine = create_engine("sqlite:///encryptor.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    encrypted_string_record = session.query(EncryptedString).filter_by(alias=alias).first()
    if encrypted_string_record:
        session.delete(encrypted_string_record)
        session.commit()
        log_activity(user=encrypted_string_record.username, activity=f"Deleted encrypted string with alias: {alias}")
        session.close()
        return True
    session.close()
    return False

def generate_user_report():
    engine = create_engine("sqlite:///encryptor.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    users = session.query(User).all()
    session.close()
    report = []
    for user in users:
        report.append({
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "phone": user.phone,
            "active_status": user.active_status,
            "alias": user.alias
        })
    return report
