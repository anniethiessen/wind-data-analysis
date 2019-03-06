import glob
import os

import pandas as pd

from .globals import *


def get_file_paths(period_dirs, scenario_dirs, forecast_dirs):
    """
    Returns a list of CSV file paths within specific period, scenario,
    and forecast directories.

    :param period_dirs: Period directory names
    :type period_dirs: list
    :param scenario_dirs: Scenario directory names
    :type scenario_dirs: list
    :param forecast_dirs: Forecast directory names
    :type forecast_dirs: list
    :return: CSV file paths
    :rtype: list

    """

    ret = []
    for period_dir in period_dirs:
        for scenario_dir in scenario_dirs:
            for forecast_dir in forecast_dirs:
                data_path = '../{r}/{p}/{s}/{f}/'.format(
                    r=ROOT_DIR, p=period_dir, s=scenario_dir, f=forecast_dir)
                ret += glob.glob(os.path.join(data_path, "*.csv"))
    return ret


def get_dataframes(file_paths):
    """
    Returns a dictionary of dataframes from list of CSV file paths.

    :param file_paths: CSV file paths
    :type file_paths: list
    :return: Dataframes
    :rtype: dict

    """

    ret = {}
    for file_path in file_paths:
        df = pd.read_csv(file_path)
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        ret[file_name] = df
    return ret


def print_heads(data_dict):
    """
    Prints file name and dataframe head (first five rows) from data
    dictionary.

    :param data_dict: File names with dataframes
    :type data_dict: dict

    """

    for file_name, df in data_dict.items():
        print('\n' + file_name + '\n')
        print(df.head())
