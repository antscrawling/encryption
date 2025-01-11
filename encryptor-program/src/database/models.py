from sqlalchemy import Column, String, Integer, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    username = Column(String, primary_key=True)
    password = Column(String, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    user_type = Column(String)  # Normal, Admin1, Admin2
    secret_question = Column(String)
    secret_answer = Column(String)
    email = Column(String)
    phone = Column(String)
    alias = Column(String)  # This can be multiple data, consider using a separate table for multiple aliases
    active_status = Column(Boolean, default=True)

class EncryptedString(Base):
    __tablename__ = 'encrypted_strings'

    alias = Column(String, primary_key=True)
    string_to_encrypt = Column(String, nullable=False)
    encrypted_string = Column(String)
    decryption_code = Column(String)
    encryption_type = Column(String)
    date_recorded = Column(DateTime, server_default=func.now())
    
    
if __name__ == "__main__":
    from sqlalchemy import create_engine
    DATABASE_URL = "sqlite:///encryptor.db"
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    print("Database tables created successfully.")