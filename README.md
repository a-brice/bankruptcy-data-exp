# bankruptcy-data-exp
**The dataset is provided by Sebastian Tomczak and collected from Emerging Markets Information Service ([EMIS](https://www.emis.com/)) :
https://archive.ics.uci.edu/ml/datasets/Polish+companies+bankruptcy+data**

***STARTER BELLOW***


The dataset is about bankruptcy prediction of Polish companies. In theses datasets, we retrieve information about emerging markets around the word (or Poland, who knows ?). A dataset is composed of thousands of rows where each row corresponds to a company. The attribute about theses companies is given in data/description.txt file. Here, is a sample of what we can have in a dataset : 


<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>bankrupt</th>
      <th><img src=formula/X1.svg></th>
      <th><img src=formula/X2.svg></th>
      <th><img src=formula/X3.svg></th>
      <th><img src=formula/X4.svg></th>
      <th><img src=formula/X5.svg></th>
      <th><img src=formula/X6.svg></th>
      <th><img src=formula/X7.svg></th>
      <th><img src=formula/X8.svg></th>
      <th><img src=formula/X9.svg></th>
      <th><img src=formula/X10.svg></th>
      <th><img src=formula/X11.svg></th>
      <th><img src=formula/X12.svg></th>
      <th><img src=formula/X13.svg></th>
      <th><img src=formula/X14.svg></th>
      <th><img src=formula/X15.svg></th>
      <th><img src=formula/X16.svg></th>
      <th><img src=formula/X17.svg></th>
      <th><img src=formula/X18.svg></th>
      <th><img src=formula/X19.svg></th>
      <th><img src=formula/X20.svg></th>
      <th><img src=formula/X21.svg></th>
      <th><img src=formula/X22.svg></th>
      <th><img src=formula/X23.svg></th>
      <th><img src=formula/X24.svg></th>
      <th><img src=formula/X25.svg></th>
      <th><img src=formula/X26.svg></th>
      <th><img src=formula/X27.svg></th>
      <th><img src=formula/X28.svg></th>
      <th><img src=formula/X29.svg></th>
      <th><img src=formula/X30.svg></th>
      <th><img src=formula/X31.svg></th>
      <th><img src=formula/X32.svg></th>
      <th><img src=formula/X33.svg></th>
      <th><img src=formula/X34.svg></th>
      <th><img src=formula/X35.svg></th>
      <th><img src=formula/X36.svg></th>
      <th><img src=formula/X37.svg></th>
      <th><img src=formula/X38.svg></th>
      <th><img src=formula/X39.svg></th>
      <th><img src=formula/X40.svg></th>
      <th><img src=formula/X41.svg></th>
      <th><img src=formula/X42.svg></th>
      <th><img src=formula/X43.svg></th>
      <th><img src=formula/X44.svg></th>
      <th><img src=formula/X45.svg></th>
      <th><img src=formula/X46.svg></th>
      <th><img src=formula/X47.svg></th>
      <th><img src=formula/X48.svg></th>
      <th><img src=formula/X49.svg></th>
      <th><img src=formula/X50.svg></th>
      <th><img src=formula/X51.svg></th>
      <th><img src=formula/X52.svg></th>
      <th><img src=formula/X53.svg></th>
      <th><img src=formula/X54.svg></th>
      <th><img src=formula/X55.svg></th>
      <th><img src=formula/X56.svg></th>
      <th><img src=formula/X57.svg></th>
      <th><img src=formula/X58.svg></th>
      <th><img src=formula/X59.svg></th>
      <th><img src=formula/X60.svg></th>
      <th><img src=formula/X61.svg></th>
      <th><img src=formula/X62.svg></th>
      <th><img src=formula/X63.svg></th>
      <th><img src=formula/X64.svg></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>0.034279</td>
      <td>0.42448</td>
      <td>-0.075832</td>
      <td>0.67532</td>
      <td>-77.334</td>
      <td>-0.01497</td>
      <td>0.044048</td>
      <td>1.3558</td>
      <td>1.1287</td>
      <td>0.57552</td>
      <td>0.044048</td>
      <td>0.1886</td>
      <td>0.11021</td>
      <td>0.044048</td>
      <td>2069.8</td>
      <td>0.17635</td>
      <td>2.3558</td>
      <td>0.044048</td>
      <td>0.064853</td>
      <td>22.179</td>
      <td>1.0305</td>
      <td>0.077574</td>
      <td>0.050469</td>
      <td>-0.016044</td>
      <td>0.57552</td>
      <td>0.15333</td>
      <td>1.2892</td>
      <td>-0.090033</td>
      <td>5.1839</td>
      <td>0.61859</td>
      <td>0.064853</td>
      <td>141.67</td>
      <td>2.5764</td>
      <td>0.18275</td>
      <td>0.077574</td>
      <td>0.67974</td>
      <td>0.60997</td>
      <td>0.76644</td>
      <td>0.11421</td>
      <td>0.04225</td>
      <td>0.12876</td>
      <td>0.11421</td>
      <td>79.459</td>
      <td>57.28</td>
      <td>0.83056</td>
      <td>0.49861</td>
      <td>25.035</td>
      <td>0.046766</td>
      <td>0.068854</td>
      <td>0.37158</td>
      <td>0.23356</td>
      <td>0.38815</td>
      <td>0.6833</td>
      <td>0.90997</td>
      <td>-11581.0</td>
      <td>0.11406</td>
      <td>0.059561</td>
      <td>0.88594</td>
      <td>0.33173</td>
      <td>16.457</td>
      <td>6.3722</td>
      <td>125.51</td>
      <td>2.908</td>
      <td>0.80639</td>
    </tr>
    <tr>
      <td>0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>0.096308&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>0.50574&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>0.48163&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>1.9523&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>229.04&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>0.096308&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>0.97731&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>3.7981&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>0.49426&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>0.15378&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>0.19043&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>0.42351&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>0.096308&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>114.76&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>3.1806&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>1.9773&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>0.096308&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>0.025357&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>6.514&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>0.60105&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>0.025357&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>0.32281&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>0.45095&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>3.1806&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>38.13&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>3.0624&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>0.026525&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>0.059985&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>85.534&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>4.2673&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>4.2673&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>0.0045052&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>3.7981&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>?&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>0.49426&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>0.0011862&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>0.80652&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>0.011148&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>55.688&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>49.174&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>1.4208&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>1.8183&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>11.464&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>-1.5122&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>-0.39815&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>1.9523&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>0.50574&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>0.23434&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>39.13&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>39.13&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>556.01&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>0.43179&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>0.19485&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>0.58486&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>56.033&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>7.4227&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>48.601&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>7.5101&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>300.69&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
    </tr>
    <tr>
      <td>0</td>
      <td>-0.20902</td>
      <td>1.2022</td>
      <td>-0.2562</td>
      <td>0.053378</td>
      <td>-108.75</td>
      <td>-0.38107</td>
      <td>-0.20902</td>
      <td>-0.16822</td>
      <td>0.82685</td>
      <td>-0.20224</td>
      <td>-0.14916</td>
      <td>-0.77232</td>
      <td>-0.098138</td>
      <td>-0.20902</td>
      <td>-5407.8</td>
      <td>-0.067495</td>
      <td>0.83178</td>
      <td>-0.20902</td>
      <td>-0.25279</td>
      <td>0</td>
      <td>?</td>
      <td>-0.14916</td>
      <td>-0.25279</td>
      <td>-0.20902</td>
      <td>-0.59009</td>
      <td>-0.067495</td>
      <td>-2.4917</td>
      <td>-0.25995</td>
      <td>2.8692</td>
      <td>1.454</td>
      <td>-0.1804</td>
      <td>101.21</td>
      <td>3.6062</td>
      <td>0.81183</td>
      <td>-0.14916</td>
      <td>0.82685</td>
      <td>0.015507</td>
      <td>0.72936</td>
      <td>-0.1804</td>
      <td>9.9866e-006</td>
      <td>-1.883</td>
      <td>-0.1804</td>
      <td>6.376</td>
      <td>6.376</td>
      <td>?</td>
      <td>0.053378</td>
      <td>0</td>
      <td>-0.27704</td>
      <td>-0.33505</td>
      <td>0.012016</td>
      <td>0.27064</td>
      <td>0.2773</td>
      <td>-0.20521</td>
      <td>0.74005</td>
      <td>-189.58</td>
      <td>-0.1804</td>
      <td>1.0335</td>
      <td>1.2528</td>
      <td>-4.6064</td>
      <td>?</td>
      <td>57.246</td>
      <td>119.47</td>
      <td>3.0551</td>
      <td>0.83897</td>
    </tr>
    <tr>
      <td>0</td>
      <td>0.20097</td>
      <td>0.19291</td>
      <td>0.23709</td>
      <td>2.229</td>
      <td>93.472</td>
      <td>0</td>
      <td>0.20097</td>
      <td>4.1836</td>
      <td>2.8936</td>
      <td>0.80709</td>
      <td>0.20097</td>
      <td>1.0418</td>
      <td>0.41244</td>
      <td>0.20097</td>
      <td>59.001</td>
      <td>6.1864</td>
      <td>5.1836</td>
      <td>0.20097</td>
      <td>0.069453</td>
      <td>9.6467</td>
      <td>0.85696</td>
      <td>0</td>
      <td>0.069453</td>
      <td>0.51819</td>
      <td>0.76878</td>
      <td>6.1864</td>
      <td>?</td>
      <td>0.41595</td>
      <td>3.7389</td>
      <td>0.040859</td>
      <td>0.15536</td>
      <td>43.706</td>
      <td>8.3512</td>
      <td>8.3512</td>
      <td>0.0066855</td>
      <td>2.8936</td>
      <td>?</td>
      <td>0.80709</td>
      <td>0.0023105</td>
      <td>0.38714</td>
      <td>0.0064793</td>
      <td>0</td>
      <td>44.82</td>
      <td>35.174</td>
      <td>2.6279</td>
      <td>1.8326</td>
      <td>17.326</td>
      <td>-0.99247</td>
      <td>-0.34299</td>
      <td>2.229</td>
      <td>0.19291</td>
      <td>0.11974</td>
      <td>1.416</td>
      <td>1.416</td>
      <td>1299.7</td>
      <td>0.44323</td>
      <td>0.24901</td>
      <td>0.55688</td>
      <td>0</td>
      <td>37.837</td>
      <td>10.377</td>
      <td>24.334</td>
      <td>14.999</td>
      <td>5.0765</td>
    </tr>
    <tr>
      <td>0</td>
      <td>-0.11132</td>
      <td>0.64559</td>
      <td>0.0041018</td>
      <td>1.0071</td>
      <td>-38.084</td>
      <td>0</td>
      <td>-0.11132</td>
      <td>0.54897</td>
      <td>2.5568</td>
      <td>0.35441</td>
      <td>-0.026645</td>
      <td>-0.19222</td>
      <td>-0.022736</td>
      <td>-0.11132</td>
      <td>-4053.6</td>
      <td>-0.090045</td>
      <td>1.549</td>
      <td>-0.11132</td>
      <td>-0.043539</td>
      <td>37.421</td>
      <td>1.0872</td>
      <td>-0.09603</td>
      <td>-0.043539</td>
      <td>-0.1175</td>
      <td>-0.085977</td>
      <td>-0.090045</td>
      <td>-1.1341</td>
      <td>0.0098424</td>
      <td>3.3675</td>
      <td>0.25123</td>
      <td>-0.033709</td>
      <td>81.987</td>
      <td>4.4519</td>
      <td>3.9938</td>
      <td>-0.021489</td>
      <td>2.5568</td>
      <td>7.0439</td>
      <td>0.4</td>
      <td>-0.0084045</td>
      <td>0.021281</td>
      <td>-0.50233</td>
      <td>-0.037558</td>
      <td>81.502</td>
      <td>44.081</td>
      <td>-0.42467</td>
      <td>0.55446</td>
      <td>37.109</td>
      <td>-0.14922</td>
      <td>-0.058361</td>
      <td>0.90344</td>
      <td>0.57915</td>
      <td>0.22462</td>
      <td>0.85041</td>
      <td>0.9598</td>
      <td>9.56</td>
      <td>-0.0084045</td>
      <td>-0.31411</td>
      <td>1.042</td>
      <td>0.12863</td>
      <td>9.7539</td>
      <td>8.2802</td>
      <td>82.676</td>
      <td>4.4148</td>
      <td>6.1352</td>
    </tr>
    <tr>
      <td>1</td>
      <td>-0.40937</td>
      <td>0.58325</td>
      <td>0.20188</td>
      <td>1.3461</td>
      <td>-0.7769</td>
      <td>0.0</td>
      <td>-0.40937</td>
      <td>0.71453</td>
      <td>9.8193</td>
      <td>0.41675</td>
      <td>-0.25112</td>
      <td>-0.70189</td>
      <td>-0.024009</td>
      <td>-0.40937</td>
      <td>-903.02</td>
      <td>-0.4042</td>
      <td>1.7145</td>
      <td>-0.40937</td>
      <td>-0.041691</td>
      <td>2.7925</td>
      <td>?</td>
      <td>-0.37487</td>
      <td>-0.041691</td>
      <td>-0.40937</td>
      <td>-0.20825</td>
      <td>-0.4042</td>
      <td>-2.3689</td>
      <td>0.94005</td>
      <td>1.9031</td>
      <td>0.016142</td>
      <td>-0.041691</td>
      <td>20.883</td>
      <td>17.478</td>
      <td>17.478</td>
      <td>-0.37487</td>
      <td>9.943</td>
      <td>?</td>
      <td>0.41675</td>
      <td>-0.038178</td>
      <td>0.98264</td>
      <td>-0.096605</td>
      <td>-0.038178</td>
      <td>7.8804</td>
      <td>5.0879</td>
      <td>-5.4493</td>
      <td>1.1114</td>
      <td>2.6898</td>
      <td>-0.5485</td>
      <td>-0.05586</td>
      <td>1.3461</td>
      <td>0.58325</td>
      <td>0.057214</td>
      <td>1.9406</td>
      <td>1.9406</td>
      <td>16.15</td>
      <td>-0.03819</td>
      <td>-0.9823</td>
      <td>1.0253</td>
      <td>0.0</td>
      <td>130.71</td>
      <td>71.739</td>
      <td>21.681</td>
      <td>16.835</td>
      <td>45.724</td>
    </tr>
    <tr>
      <td>1</td>
      <td>-0.19899</td>
      <td>0.42164</td>
      <td>0.57836</td>
      <td>2.3717</td>
      <td>50.094</td>
      <td>-0.20152</td>
      <td>-0.19899</td>
      <td>1.3717</td>
      <td>3.9931</td>
      <td>0.57836</td>
      <td>-0.19797</td>
      <td>-0.47193</td>
      <td>-0.041069</td>
      <td>-0.19899</td>
      <td>-938.46</td>
      <td>-0.38893</td>
      <td>2.3717</td>
      <td>-0.19899</td>
      <td>-0.049833</td>
      <td>0</td>
      <td>?</td>
      <td>-0.19831</td>
      <td>-0.049833</td>
      <td>-0.19899</td>
      <td>-0.38529</td>
      <td>-0.38893</td>
      <td>-195.5</td>
      <td>?</td>
      <td>1.772</td>
      <td>-0.054405</td>
      <td>-0.049833</td>
      <td>36.719</td>
      <td>9.9407</td>
      <td>9.9407</td>
      <td>-0.19831</td>
      <td>3.9932</td>
      <td>?</td>
      <td>0.57836</td>
      <td>-0.049663</td>
      <td>1.5152</td>
      <td>-0.086059</td>
      <td>-0.049663</td>
      <td>33.009</td>
      <td>33.009</td>
      <td>?</td>
      <td>1.5152</td>
      <td>0</td>
      <td>-0.23331</td>
      <td>-0.058428</td>
      <td>2.3717</td>
      <td>0.42164</td>
      <td>0.1006</td>
      <td>?</td>
      <td>?</td>
      <td>34.21</td>
      <td>-0.049621</td>
      <td>-0.34405</td>
      <td>1.0496</td>
      <td>0.0</td>
      <td>?</td>
      <td>11.058</td>
      <td>38.541</td>
      <td>9.4703</td>
      <td>?</td>
    </tr>
    <tr>
      <td>1</td>
      <td>0.14806</td>
      <td>0.83471</td>
      <td>-0.050636</td>
      <td>0.8059</td>
      <td>-43.448</td>
      <td>-0.34617</td>
      <td>0.16452</td>
      <td>0.19804</td>
      <td>0.82432</td>
      <td>0.16531</td>
      <td>0.22872</td>
      <td>0.63064</td>
      <td>0.26792</td>
      <td>0.16452</td>
      <td>1379.5</td>
      <td>0.26459</td>
      <td>1.198</td>
      <td>0.16452</td>
      <td>0.19958</td>
      <td>25.982</td>
      <td>?</td>
      <td>0.2287</td>
      <td>0.17961</td>
      <td>0.16452</td>
      <td>-0.19827</td>
      <td>0.24487</td>
      <td>3.5621</td>
      <td>-0.064112</td>
      <td>3.5149</td>
      <td>0.95298</td>
      <td>0.20139</td>
      <td>94.239</td>
      <td>3.8957</td>
      <td>1.2175</td>
      <td>-0.18627</td>
      <td>1.2451</td>
      <td>0.28541</td>
      <td>0.69632</td>
      <td>-0.22597</td>
      <td>0.21346</td>
      <td>0.097614</td>
      <td>0.27744</td>
      <td>68.433</td>
      <td>42.451</td>
      <td>2.5232</td>
      <td>0.43839</td>
      <td>21.074</td>
      <td>0.17236</td>
      <td>0.2091</td>
      <td>0.25187</td>
      <td>0.26087</td>
      <td>0.25669</td>
      <td>0.2093</td>
      <td>0.88164</td>
      <td>-165.73</td>
      <td>-0.22572</td>
      <td>0.89565</td>
      <td>0.81625</td>
      <td>3.2123</td>
      <td>14.048</td>
      <td>8.5981</td>
      <td>115.51</td>
      <td>3.1599</td>
      <td>1.0437</td>
    </tr>
    <tr>
      <td>1</td>
      <td>-0.092469</td>
      <td>0.8223</td>
      <td>-0.18051</td>
      <td>0.75948</td>
      <td>-200.23</td>
      <td>0.0</td>
      <td>-0.096245</td>
      <td>0.2161</td>
      <td>1.1797</td>
      <td>0.1777</td>
      <td>-0.059312</td>
      <td>-0.12824</td>
      <td>-0.046759</td>
      <td>-0.096245</td>
      <td>-5441.4</td>
      <td>-0.067079</td>
      <td>1.2161</td>
      <td>-0.096245</td>
      <td>-0.081588</td>
      <td>126.65</td>
      <td>0.98898</td>
      <td>-0.07112</td>
      <td>-0.078387</td>
      <td>0.91179</td>
      <td>0.088247</td>
      <td>-0.062487</td>
      <td>-1.9257</td>
      <td>-0.41978</td>
      <td>4.4644</td>
      <td>0.68549</td>
      <td>-0.058165</td>
      <td>258.64</td>
      <td>1.4744</td>
      <td>1.3456</td>
      <td>-0.079529</td>
      <td>1.1797</td>
      <td>5.0715</td>
      <td>0.20938</td>
      <td>-0.067417</td>
      <td>0.021861</td>
      <td>-0.91265</td>
      <td>-0.060289</td>
      <td>171.28</td>
      <td>44.637</td>
      <td>-0.22591</td>
      <td>0.21409</td>
      <td>135.02</td>
      <td>-0.11221</td>
      <td>-0.095118</td>
      <td>0.69316</td>
      <td>0.7505</td>
      <td>0.67826</td>
      <td>0.41323</td>
      <td>0.48691</td>
      <td>-5259</td>
      <td>0.10219</td>
      <td>-0.52038</td>
      <td>0.9693</td>
      <td>0.17829</td>
      <td>2.882</td>
      <td>8.177</td>
      <td>232.21</td>
      <td>1.5718</td>
      <td>2.7433</td>
    </tr>
    <tr>
      <td>1</td>
      <td>-0.006009</td>
      <td>0.87154</td>
      <td>-0.30285</td>
      <td>0.65251</td>
      <td>-20.725</td>
      <td>-2.1532</td>
      <td>-0.006009</td>
      <td>0.14746</td>
      <td>5.5023</td>
      <td>0.12852</td>
      <td>0.12882</td>
      <td>-0.0068951</td>
      <td>0.018794</td>
      <td>-0.006009</td>
      <td>3076.2</td>
      <td>0.11865</td>
      <td>1.1474</td>
      <td>-0.006009</td>
      <td>-0.0010922</td>
      <td>0.0078939</td>
      <td>?</td>
      <td>0.12882</td>
      <td>-0.0010922</td>
      <td>-0.006009</td>
      <td>-2.1592</td>
      <td>0.11865</td>
      <td>0.95543</td>
      <td>-0.70217</td>
      <td>2.2255</td>
      <td>0.10544</td>
      <td>-0.0010381</td>
      <td>57.891</td>
      <td>6.305</td>
      <td>6.305</td>
      <td>0.007199</td>
      <td>5.6238</td>
      <td>?</td>
      <td>0.12852</td>
      <td>0.0013084</td>
      <td>0.34244</td>
      <td>0.12194</td>
      <td>0.023411</td>
      <td>17.927</td>
      <td>17.919</td>
      <td>-50.5</td>
      <td>0.34257</td>
      <td>0.0079043</td>
      <td>0.019397</td>
      <td>0.0035252</td>
      <td>0.65251</td>
      <td>0.87154</td>
      <td>0.15861</td>
      <td>0.29797</td>
      <td>0.29797</td>
      <td>-50.9</td>
      <td>0.0013192</td>
      <td>-0.046759</td>
      <td>0.97709</td>
      <td>0.0</td>
      <td>46239</td>
      <td>20.369</td>
      <td>57.815</td>
      <td>6.3133</td>
      <td>12.757</td>
    </tr>
  </tbody>
</table>

We are in a case of supervised learning, a classification with labelled data which indicates whether the company bankrupted or not.


The goal of this project is to explore, analyse and make data visualisation before applying machine learning algorithms in order to predict and classify, with the best accuracy, the situation of a company. 


In total in this dataset, we have more than 43 000 companies' status inequitably distributed on 5 years. The columns represent the **64 variables** we will use to predict bankruptcy. Among these variables, we can see there is underlying variables which appear and impact a lot of variables, like total assets, total liabilities, net profit and much more that we can use directly in order to have fewer variables to include in our model without loss of information. We can also see there is multiple missing values symbolised by a **"?"** in many fields.
 
 
 
<h3>To launch the API</h3>
<hr>

Start to clone the project : 

```sh
git clone https://github.com/a-brice/bankruptcy-data-exp.git
cd bankruptcy-data-exp
```

To launch the API, you must install some dependencies first. (Window) From a shell from the root directory, enter the following :

```sh
python -m venv env
.\env\Scripts\activate
pip install -r requirement.txt
```

When all installations are completed (a bit long), you can now run the API :

```sh
cd api
python manage.py runserver
```
And after that, go to http://127.0.0.1:8000 and explore !
 
