from database.models import User
from utils.logger import log_activity

def view_user_profile(username):
    user = User.query.filter_by(username=username).first()
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
    user = User.query.filter_by(username=username).first()
    if user:
        user.active_status = False
        log_activity(username, "Deactivated own profile")
        return True
    return False

def update_user_profile(username, first_name=None, last_name=None, email=None, phone=None):
    user = User.query.filter_by(username=username).first()
    if user:
        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        if email:
            user.email = email
        if phone:
            user.phone = phone
        log_activity(username, "Updated profile information")
        return True
    return False