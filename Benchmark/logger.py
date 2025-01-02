import logging
import os

# Create logs directory if it doesn't exist
LOG_DIR = "Benchmark/logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Set up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create file handler that logs debug and higher level messages
file_handler = logging.FileHandler(os.path.join(LOG_DIR, 'app.log'))
file_handler.setLevel(logging.DEBUG)

# Create console handler that logs warning and higher level messages
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)

# Create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

def get_logger():
    return logger
