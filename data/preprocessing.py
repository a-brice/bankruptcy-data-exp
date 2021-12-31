import pandas as pd 
import numpy as np
import pathlib 
import os, json

def to_csv(path):
    """Get the .arff data to CSV format"""
    dirpath = pathlib.Path(path)
    files = dirpath.rglob('*.arff')
    
    if not os.path.exists(dirpath / 'csv'):
        os.mkdir(dirpath / 'csv')
    
        for file in files:
            df = pd.read_csv(file, skiprows=69)
            df.columns = [f'X{i}' for i in range(1, df.shape[1]+1)]
            df.to_csv(dirpath / 'csv/{0}.csv'.format(file.stem), index=False)
  
            

def description_format():
    """Get the JSON Description"""
    dic = {}
    with open('description.txt', 'r') as f:
        for line in f:
            col, *desc = line.split()
            desc = ' '.join(desc)
            dic[col] = desc
            
    with open('description.json', 'w') as f:
        f.write(json.dumps(dic, indent=4))
          
  

def big_dataset(path):
    """Get the data.csv which is the concatenation of the 5 files"""
    files = list(pathlib.Path(path).rglob('*year.csv'))
    
    data = [pd.read_csv(file).assign(year=file.stem) for file in files]
    data = pd.concat(data, ignore_index=True)
    data = data[['year', *data.columns.drop('year')]]
    
    data.to_csv(path + 'csv/data.csv', index=False)
    
    
            
if __name__ == '__main__':
    path = './extension/'
    # to_csv(path)
    # description_format()
    # big_dataset(path)