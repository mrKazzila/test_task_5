import logging
from pathlib import Path

import pandas as pd
from pandas import DataFrame

from src.project_dataclasses import CsvFields

logger = logging.getLogger(__name__)


def csv_handler(path: Path, delimiter: str) -> DataFrame:
    """
    Process a CSV file and perform calculations on its data.

    Args:
        path (Path): The path to the CSV file.
        delimiter (str): The delimiter used in the CSV file.

    Returns:
        DataFrame: A DataFrame containing the calculated results.

    Raises:
        FileNotFoundError: If the specified file path does not exist.
    """
    df = _to_df_from_csv(path=path, delimiter=delimiter)
    logger.debug('successfully read data from csv')

    years = _get_years_from_df(dataframe=df)
    logger.debug(
        'got a list of years %(count_years)s from the dataframe',
        {'count_years': len(years)},
    )

    terminal_nodes = _get_terminal_nodes(dataframe=df, years=years)
    logger.debug(
        'created dataframe with terminal nodes, count= %(count_nodes)s',
        {'count_nodes': len(terminal_nodes)},
    )

    non_terminal_nodes = _get_non_terminal_nodes(dataframe=df, years=years)
    logger.debug(
        'created dataframe with non terminal nodes, count=%(count_nodes)s',
        {'count_nodes': len(non_terminal_nodes)},
    )

    result_df = pd.DataFrame(columns=df.columns)
    result = _calculation(
        result_df=result_df,
        terminal=terminal_nodes,
        non_terminal=non_terminal_nodes,
        years=years,
    )

    logger.debug(
        'create dataframe with results, count=%(count)s',
        {'count': len(result)},
    )

    return result


def _to_df_from_csv(path: Path, delimiter: str = ';') -> DataFrame:
    """
    Read data from a CSV file and return it as a DataFrame.

    Args:
        path (Path): The path to the CSV file.
        delimiter (str, optional): The delimiter used in the CSV file. Default is ';'.

    Returns:
        DataFrame: The data from the CSV file as a DataFrame.

    Raises:
        FileNotFoundError: If the specified file path does not exist.
    """
    return pd.read_csv(path, sep=delimiter)


def _get_years_from_df(dataframe: DataFrame) -> list:
    """
    Extract the years from the columns of a DataFrame.

    Args:
        dataframe (DataFrame): The input DataFrame.

    Returns:
        list: A list of years extracted from the DataFrame columns.
    """
    return [col for col in dataframe.columns if col.isdigit()]


def _get_terminal_nodes(dataframe: DataFrame, years: list) -> DataFrame:
    """
    Get the terminal nodes from the DataFrame.

    Args:
        dataframe (DataFrame): The input DataFrame.
        years (list): List of years.

    Returns:
        DataFrame: DataFrame containing terminal nodes.
    """
    return dataframe[dataframe[years].notna().any(axis=1)]


def _get_non_terminal_nodes(dataframe: DataFrame, years: list) -> DataFrame:
    """
    Get the non-terminal nodes from the DataFrame.

    Args:
        dataframe (DataFrame): The input DataFrame.
        years (list): List of years.

    Returns:
        DataFrame: DataFrame containing non-terminal nodes.
    """
    return dataframe[dataframe[years].isna().any(axis=1)]


def _calculation(
        result_df: DataFrame,
        terminal: DataFrame,
        non_terminal: DataFrame,
        years: list,
) -> DataFrame:
    """
    Perform calculations for terminal and non-terminal nodes and return the result.

    Args:
        result_df (DataFrame): An empty DataFrame to store the results.
        terminal (DataFrame): DataFrame containing terminal nodes.
        non_terminal (DataFrame): DataFrame containing non-terminal nodes.
        years (list): List of years.

    Returns:
        DataFrame: DataFrame containing the calculated results.
    """
    for _, non_terminal_row in non_terminal.iterrows():
        code = non_terminal_row[CsvFields.code]

        related_terminals = terminal[terminal[CsvFields.code].str.startswith(code)]
        sums = related_terminals[years].sum()

        new_row = non_terminal_row.copy()
        new_row[years] = sums

        result_df = pd.concat([result_df, new_row.to_frame().transpose()], ignore_index=True)

    return result_df


if __name__ == '__main__':
    from settings import CSV_FILE, DELIMITER  # noqa, just for module running

    result_ = csv_handler(path=CSV_FILE, delimiter=DELIMITER)
    logger.info(
        'Results: \n %(result)s',
        {'result': result_},
    )
