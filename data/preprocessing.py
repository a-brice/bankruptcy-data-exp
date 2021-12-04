import pandas as pd 
import numpy as np
import pathlib 
import os, json

def to_csv(path):
    dirpath = pathlib.Path(path)
    files = dirpath.rglob('*.arff')
    
    if not os.path.exists(dirpath / 'csv'):
        os.mkdir(dirpath / 'csv')
    
        for file in files:
            df = pd.read_csv(file, skiprows=69)
            df.columns = [f'X{i}' for i in range(1, df.shape[1]+1)]
            df.to_csv(dirpath / 'csv/{0}.csv'.format(file.stem), index=False)
  
            

def description_format():
    dic = {}
    with open('description.txt', 'r') as f:
        for line in f:
            col, *desc = line.split()
            desc = ' '.join(desc)
            dic[col] = desc
            
    with open('description.json', 'w') as f:
        f.write(json.dumps(dic, indent=4))
          
  
    
            
if __name__ != '__main__':
    path = './extension/'
    to_csv(path)
    description_format()