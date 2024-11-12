import os
import logging
from datetime import datetime


# Define log file name with timestamp
log_file_name = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"

# Define the path where logs will be stored
log_dir = os.path.join(os.getcwd(), "logs")

# Create the log directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Full path for the log file
log_file_path = os.path.join(log_dir, log_file_name)

# Set up the logging configuration
logging.basicConfig(
    filename=log_file_path,  # Corrected 'file_name' to 'filename'
    format="[(%(asctime)s)] %(lineno)d %(name)s - %(levelname)s - %(message)s",  # Corrected 'formate' to 'format'
    level=logging.INFO,
)

