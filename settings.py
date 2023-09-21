import logging
from pathlib import Path

# Path settings
_FILE = Path(__file__)
_DIR = _FILE.parent
_DATA_DIR = _DIR / 'data'

CSV_FILE = _DATA_DIR / 'data.csv'

# CSV settings
DELIMITER = ';'

# DB settings
DB_URL = 'postgresql://postgres:postgres@localhost:6432/test_task_result'
DB_TABLE_NAME = 'results'
DB_IF_TABLE_EXIST = 'replace'

# Logging settings
_LOG_LEVEL = logging.DEBUG
_LOG_FORMAT = '[%(asctime)s] %(levelname)s [%(module)s:%(lineno)s] %(message)s'
_LOG_DATA_FORMAT = '%d-%b-%Y %H:%M:%S'

logging.basicConfig(
    level=_LOG_LEVEL,
    datefmt=_LOG_DATA_FORMAT,
    format=_LOG_FORMAT,
    encoding='utf-8',
)
