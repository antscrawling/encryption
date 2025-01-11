from sqlalchemy.orm import sessionmaker
from database.db_setup import create_engine, User

def login(username, password):
    engine = create_engine("sqlite:///encryptor.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    user = session.query(User).filter_by(username=username, password=password).first()
    session.close()

    if user:
        return True
    return False
