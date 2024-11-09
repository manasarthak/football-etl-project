# main.py
import os
import logging

# Set up logging to file
logging.basicConfig(
    filename='etl_workflow.log',  # Log file name
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info('Starting ETL workflow...')

try:
    # Run the 'push_to_blob.py' script and log output
    if os.system('python push_to_blob.py') != 0:
        logging.error("Error running push_to_blob.py")

    # Run the 'push_to_sqlite.py' script and log output
    if os.system('python push_to_sqlite.py') != 0:
        logging.error("Error running push_to_sqlite.py")

except Exception as e:
    logging.exception("An error occurred during the ETL workflow")

logging.info('ETL workflow completed.')
