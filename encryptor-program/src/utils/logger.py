def log_activity(user, activity):
    from datetime import datetime
    log_date = datetime.now().date()
    log_time = datetime.now().time()
    
    with open('activity_log.txt', 'a') as log_file:
        log_file.write(f"{log_date} {log_time} - User: {user}, Activity: {activity}\n")

def generate_log_report():
    try:
        with open('activity_log.txt', 'r') as log_file:
            return log_file.readlines()
    except FileNotFoundError:
        return "No log file found."