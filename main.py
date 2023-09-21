import logging

from settings import CSV_FILE, DELIMITER
from src.data_handler import csv_handler
from src.database import insert_df_to_db_table
from src.exceptions import IncorrectHandelDataException

logger = logging.getLogger(__name__)


def main():
    """Main function for run script."""

    handel_data_from_csv = csv_handler(
        path=CSV_FILE,
        delimiter=DELIMITER,
    )

    if handel_data_from_csv is None or handel_data_from_csv.empty:
        raise IncorrectHandelDataException(f'Error: {handel_data_from_csv=}')

    logger.info('get handel data from csv')
    logger.info(
        'Results: \n %(result)s',
        {'result': handel_data_from_csv},
    )

    insert_df_to_db_table(
        table_name='results',
        data=handel_data_from_csv,
    )
    logger.info('insert data to database')


if __name__ == '__main__':
    logger.info('start program')
    main()
    logger.info('end program')
