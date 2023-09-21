from pandas import DataFrame
from sqlalchemy import create_engine

from settings import DB_URL, DB_IF_TABLE_EXIST

engine = create_engine(DB_URL)


def insert_df_to_db_table(table_name: str, data: DataFrame) -> None:
    """
    Insert Dataframe into database table.

    Args:
        table_name (str): The table name.
        data (DataFrame): The Dataframe with data.
    """
    with engine.connect() as connection:
        data.to_sql(
            table_name,
            con=connection,
            if_exists=DB_IF_TABLE_EXIST,
            index=False,
        )
