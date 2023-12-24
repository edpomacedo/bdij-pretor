# Pretor/1.0 - @edpomacedo - utils/logger.py
import logging
import os

log_filename = os.path.join(os.getcwd(), 'logs', 'uploader.log')
os.makedirs(os.path.join(os.getcwd(), 'logs'), exist_ok=True)
logging.basicConfig(filename=log_filename, level=logging.INFO, format='[%(asctime)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

logger = logging.getLogger(__name__)
