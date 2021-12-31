import pandas as pd
import numpy as np


def data_prep(path):
    data = pd.read_csv(path)
    missing = (data == '?')
    
    # Drop variable and company with too many missing values
    useless_col = missing.sum(axis=0)[missing.sum(axis=0) > 1000].index
    useless_row = missing.sum(axis=1)[missing.sum(axis=1) > 10].index
    data.drop(columns=useless_col, index=useless_row, inplace=True)
    
    # Replace the remaining missing values by the mean depending of the year and the bankrupt
    data.replace('?', np.NAN, inplace=True)
    data[data.columns.drop(['year', 'X65'])] = data[data.columns.drop(['year', 'X65'])].astype(float)
    data[['year', 'X65']] = data[['year', 'X65']].astype('category')
    
    data.fillna(data.mean(), inplace=True)
    
    return data
