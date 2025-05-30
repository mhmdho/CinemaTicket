import time
import logging
from django.db import connection
from django.core.management import call_command


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('db_wait')

def wait_for_postgres():
    while True:
        try:
            connection.ensure_connection()
            logger.info("Database connected")
            break
        except Exception as e:
            logger.info("Database unavailable, waiting...")
            time.sleep(2)

if __name__ == "__main__":
    wait_for_postgres()
    call_command('migrate', '--noinput')
