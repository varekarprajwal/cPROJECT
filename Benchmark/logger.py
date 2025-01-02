import logging
from logging.handlers import RotatingFileHandler
import os

LOG_DIR = "Benchmark/logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

def get_logger():
    # Set up the logger with both console and file handlers
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    
    # Console logging
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # File logging with rotation
    file_handler = RotatingFileHandler(f'{LOG_DIR}/program.log', maxBytes=10*1024*1024, backupCount=5)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return logger
