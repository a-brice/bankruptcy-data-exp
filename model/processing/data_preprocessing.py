import pandas as pd


def data_prep():
    data = pd.read_csv('../../data/extension/csv/data.csv')
    return data