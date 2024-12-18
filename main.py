# Modules
from func import logger
from func import core

# Views
from views import login

# Start logging system
logger.log_info("System Start")

# Start files
logger.log_info("Start files")
core.start_files()

# Main thread
login.login('Jorge', 'Jorge')
login.register('Jorge', 'Jorge')

login.delete("Jorge", "jorge")