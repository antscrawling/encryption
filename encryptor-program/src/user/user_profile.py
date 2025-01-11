from database.models import User
from utils.logger import log_activity
from sqlalchemy.orm import sessionmaker
from database.db_setup import create_engine

def view_user_profile(username):
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

def deactivate_user(username):
    engine = create_engine("sqlite:///encryptor.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    user = session.query(User).filter_by(username=username).first()
    if user:
        user.active_status = False
        session.commit()
        log_activity(username, "Deactivated own profile")
        session.close()
        return True
    session.close()
    return False

def update_user_profile(username, first_name=None, last_name=None, email=None, phone=None):
    engine = create_engine("sqlite:///encryptor.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    user = session.query(User).filter_by(username=username).first()
    if user:
        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        if email:
            user.email = email
        if phone:
            user.phone = phone
        session.commit()
        log_activity(username, "Updated profile information")
        session.close()
        return True
    session.close()
    return False
