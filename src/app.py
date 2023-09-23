from random import randint
from time import sleep
from datetime import datetime
import os
import logging
import pytz

from dbutils import transactional, get_conn

from settings import DSN

tz = pytz.timezone('Europe/Madrid')

logging.basicConfig(
    format='%(asctime)s [%(levelname)s] %(message)s',
    level='INFO',
    datefmt='%d/%m/%Y %X')

logger = logging.getLogger(__name__)


def persists(key, dt, status):
    with transactional(conn=get_conn(DSN)) as db:
        seq_log = db.fetch_all("SELECT nextval('seq_measurementlog')")[0][0]
        db.insert('measurementlog', dict(
            id=seq_log,
            key=key,
            datetime=dt,
            status=status
        ))


KEY = os.getenv('KEY')
status = 0
while True:
    now = datetime.now(tz)
    persists(
        key=KEY,
        dt=now,
        status=status
    )
    logger.info(f"[{now}] status: {status}")
    status = 1 if status == 0 else 0
    sleep(randint(5, 15))
