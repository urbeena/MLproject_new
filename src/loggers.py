import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)
logging.basicConfig(

    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(levelname)s -%(lineno)d- %(message)s",
    level=logging.INFO,
)

if __name__=="__main__":
    logging.info("Logging has been set up.")



'''
asctime is a function in Python's time module 
that converts a time tuple (or current local time)
into a human-readable string.
import time

print(time.asctime())
output:Thu Dec  4 14:48:29 2025

'''