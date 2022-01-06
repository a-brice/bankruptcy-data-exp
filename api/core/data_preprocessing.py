import pandas as pd 
import numpy as np
import pathlib 
import os, json


def data_preparation(data, option):
    data[data == '?'] = np.NAN
    data = data.astype(float)

    if  option == 2:
        useless_col = ['X21', 'X37']
        data.drop(useless_col, axis=1, inplace=True)
        data.fillna(data.mean(), inplace=True)
    
    if option == 3:
        data = underlying_data(data)
    
    return data





def underlying_data(data):
    """ Get the underlying variable of a dataset """
    # first start to extract total assets variables
    # This is the easiest way to start because we have the 'logarithm of total assets' which is X29

    newdata = pd.DataFrame()
    
    newdata['U1'] = np.exp(data.X29.values)
    
    # Then net profit 
    newdata['U2'] = newdata.U1 * data.X1
    
    # total liabilities
    newdata['U3'] = newdata.U1 * data.X2
    
    # working capital
    newdata['U4'] = newdata.U1 * data.X3
    
    # retained earnings
    newdata['U5'] = newdata.U1 * data.X6
    
    # EBIT 
    newdata['U6'] = newdata.U1 * data.X7
    
    # book value of equity
    newdata['U7'] = newdata.U3 * data.X8
    
    # sales
    newdata['U8'] = newdata.U1 * data.X9
    
    # equity
    newdata['U9'] = newdata.U1 * data.X10
    
    # gross profit
    newdata['U10'] = newdata.U1 * data.X18
    
    # short-term liabilities
    newdata['U11'] = newdata.U10 * (1/data.X12)
    
    # depreciation
    newdata['U12'] = (data.X13 * newdata.U8) - newdata.U10
    
    # interest
    newdata['U13'] = (data.X14 * newdata.U1) - newdata.U10
    
    # inventory
    newdata['U14'] = (data.X20 * newdata.U8) / 365
    
    # profit on operating activities
    newdata['U15'] = newdata.U1 * data.X22 
    
    # gross profit (in 3 years)
    newdata['U16'] = newdata.U1 * data.X24
    
    # share capital
    newdata['U17'] = newdata.U9 - (newdata.U1 * data.X25)
    
    # financial expenses
    newdata['U18'] = newdata.U15 * (1/data.X27)
    
    # fixed assets
    newdata['U19'] = newdata.U4 * (1/data.X28)
    
    # cash
    newdata['U20'] = newdata.U3 - (data.X30 * newdata.U8)
    
    # operating expenses
    newdata['U21'] = newdata.U11 * data.X33
    
    # profit on sales
    newdata['U22'] = newdata.U1 * data.X35
    
    # total sales
    newdata['U23'] = newdata.U1 * data.X36
    
    # constant capital
    newdata['U24'] = newdata.U1 * data.X38
    
    # profit on sales
    newdata['U25'] = newdata.U8 * data.X39
    
    # current assets
    newdata['U26'] = (newdata.U11 * data.X46) + newdata.U14
    
    # cost of products sold
    newdata['U27'] = newdata.U14 * (365/data.X47)
    
    # EBITDA 
    newdata['U28'] = (newdata.U1 * data.X48) / (newdata.U15 - newdata.U12)
    
    # total costs
    newdata['U29'] = newdata.U23 * data.X58
    
    # long-term liabilities
    newdata['U30'] = newdata.U9 * data.X59
    
    # receivables
    newdata['U31'] = newdata.U8 * (1/data.X59)
    
    # current liabilities
    newdata['U32'] = newdata.U27 * data.X32 / 365
    
    # sales (n) / sales (n-1)
    newdata['U33'] = data.X21
    
    # rotation receivables + inventory turnover in days
    newdata['U34'] = data.X43
    

    newdata.replace(np.inf, np.NAN, inplace=True)
    newdata.fillna(newdata.mean(), inplace=True)
    useless_col = ['U18', 'U31', 'U33']
    newdata.drop(columns=useless_col, inplace=True)

    
    return newdata

