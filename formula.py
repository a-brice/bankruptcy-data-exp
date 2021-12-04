import pandas as pd 
import numpy as np
import pathlib 
import os, json, re

# save formula images (for readme file)
def formula():
    import requests as r
    with open('data/description.json') as f:
        dic = json.load(f)
    
    for k,v in dic.items():
        val = [val.replace(' + ', '%2B').replace(' ', '\\,'*2).replace('*', '\\times')
               for val in v.split('/')] 
        
        if not k in ['X5', 'X21', 'X24']:
            val = [v.replace('(', '').replace(')', '') for v in val]
        
        val = '\\LARGE \\frac{' + '}{'.join(val) + '}' #formula 
        val = 'https://render.githubusercontent.com/render/math?math={}'.format(val) #url 
        dic[k] = val
    
    for key, url in dic.items():
        img = r.get(url).content
        with open(f'formula/{key}.svg', 'wb') as f:
            f.write(img)


#create readme table 
def table():
    example_path = './data/extension/csv/2year.csv'
    table = pd.read_csv(example_path)
    table = pd.concat([table[table.X65 == 0].sample(5), table[table.X65 == 1].sample(5)])

    images = [str(img).replace('\\','/') for img in pathlib.Path('formula/').glob('*.svg')]
    images.sort(key=lambda x: int(re.search('\d+', x).group()))
    images = [f'<img src={img}>' for img in images] + ['bankrupt']
    table.columns = images
    table.iloc[1] = [str(x) + '&nbsp;'*40 for x in table.iloc[1].values] #.map(lambda x:  're&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;' + str(x) + '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;')
    table = table.reindex(columns=['bankrupt'] + images[:-1])
    print(table.shape)
    table.to_html('sample.html', escape=False, index=False)
    

if __name__ == '__main__':
    #formula()
    table()