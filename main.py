import glob
import os

import pandas as pd
# import numpy as np


root_dir = 'data'
years_dirs = ['2008-2010']
time_dirs = ['actual']
type_dirs = ['targeted35']


def test():
    for years_dir in years_dirs:
        for time_dir in time_dirs:
            for type_dir in type_dirs:
                data_path = './{root}/{years}/{time}/{type}/'.format(
                    root=root_dir,
                    years=years_dir,
                    time=time_dir,
                    type=type_dir
                )
                files = glob.glob(os.path.join(data_path, "*.csv"))

                data = {}
                for file in files:
                    df = pd.read_csv(file)
                    file_name = os.path.splitext(os.path.basename(file))[0]
                    data[file_name] = df
                for k, v in data.items():
                    print('\n' + k + '\n')
                    print(v.head())
