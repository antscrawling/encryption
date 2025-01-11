from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database setup
DATABASE_URL = "sqlite:///encryptor.db"  # Change this to your preferred database URL

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    username = Column(String, primary_key=True)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    user_type = Column(String)  # Normal, Admin1, Admin2
    secret_question = Column(String)
    secret_answer = Column(String)
    email = Column(String)
    phone = Column(String)
    alias = Column(String)  # This can be multiple data
    active_status = Column(Boolean, default=True)

class EncryptedString(Base):
    __tablename__ = 'encrypted_strings'
    
    alias = Column(String, primary_key=True)
    string_to_encrypt = Column(String)
    encrypted_string = Column(String)
    decryption_code = Column(String)
    encryption_type = Column(String)
    record_date = Column(String)  # Date of this record tied to the alias
    username = Column(String)  # Add username to track who encrypted the string

def setup_database():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)()  # Return a session object for database operations

def save_encrypted_string(alias, encrypted_string, decryption_code, encryption_type, record_date, username):
    session = setup_database()
    encrypted_string = EncryptedString(alias=alias, encrypted_string=encrypted_string, decryption_code=decryption_code, encryption_type=encryption_type, record_date=record_date, username=username)
    session.add(encrypted_string)
    session.commit()
    session.close()

if __name__ == "__main__":
    setup_database()
    print("Database tables created successfully.")
    
    #save to encrypted_strings
    #save_encrypted_string(alias, encrypted_string, decryption_code,encryption_type,record_date)

