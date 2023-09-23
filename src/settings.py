import os
from pathlib import Path

from dotenv import load_dotenv

ENVIRONMENT = os.getenv('ENVIRON', 'local')

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(dotenv_path=Path(BASE_DIR).resolve().joinpath('env', ENVIRONMENT, '.env'))

INFLUXDB_MEASUREMENT = 'measurement1'

DSN = f"dbname='{os.getenv('POSTGRES_NAME')}' user='{os.getenv('POSTGRES_USER')}' host='{os.getenv('POSTGRES_HOST')}' password='{os.getenv('POSTGRES_PASS')}' port='{os.getenv('POSTGRES_PORT')}'"
