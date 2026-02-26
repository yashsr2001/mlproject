import logging
import sys
import os
from datetime import datetime

LOG_FILE = f"logs/{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
LOG_DIR = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

if __name__ == "__main__":
    logging.info("Logger is set up and ready to use.")