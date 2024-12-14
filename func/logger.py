"""
Logger all user activity
"""

# Modules
from datetime import datetime

# Get current time
def current_time() -> str:
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Log Base Message
def log_message(level:str, message:str) -> None:
    # Message format
    log_entry = f'{current_time()} - {level} - {message}\n'

    with open('logs.txt', 'a') as file:
        file.write(log_entry)
        file.close
    
    return log_entry

# Debug
def log_debug(message: str) -> str:
    return log_message("DEBUG", message)

# Info
def log_info(message: str) -> str:
    return log_message("INFO", message)

# Warning
def log_warning(message: str) -> str:
    return log_message("WARNING", message)

# Error
def log_error(message: str) -> str:
    return log_message("ERROR", message)