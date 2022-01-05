from django.shortcuts import redirect, render, HttpResponse
from django.core.files.storage import FileSystemStorage
import pandas as pd
import numpy as np
from django.conf import settings
from plotly.offline import plot
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import plotly.express as px
import json
from .data_preprocessing import data_preparation, underlying_data


# Data importation
data = pd.read_csv('./static/data.csv')
data[data == '?'] = np.NAN
data[data.columns.drop('year')] = data[data.columns.drop('year')].astype(float)

udata = pd.read_csv('./static/udata.csv')


with open('./static/description.json', 'r') as f:
    desc = json.loads(f.read())
    desc['X65'] = 'bankrupt'


with open('./static/udata_description.json', 'r') as f:
    udesc = json.loads(f.read())
    udesc['U35'] = 'bankrupt'
    
    
udata.columns = udata.columns.map(
    lambda x: udesc.get(x) if x != 'year' else 'year'
)
col = [*udata.columns[-2:], *udata.columns[:-2]]
udata = udata[col]



def index(req):
    return render(req, 'core/index.html')

def viz(req):
    context = {}
    data.X65 = data.X65.astype('category')
    context['total_nb'] = len(data)
    
    # LinePlot
    nb_bankrupt = data[data.X65 == 1].value_counts('year').sort_index()
    
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(
        go.Scatter(
            x=nb_bankrupt.index,
            y=nb_bankrupt.values,
            name='Number of bankrupt companies'
        ), secondary_y=False)

    fig.add_trace(
        go.Scatter(
            x=nb_bankrupt.index,
            y=nb_bankrupt.values / data.year.value_counts().sort_index(),
            name="Proportion of bankrupt companies"
        ), secondary_y=True)

    fig.update_layout(
        legend={'xanchor':'left','yanchor':'top', 'orientation':'h'},
        title='Bankruptcy'
    )

    context['line_plot'] = plot(fig, output_type='div')

    # PiePlot
    fig = go.Figure()
    fig.add_trace(go.Pie(labels=nb_bankrupt.index, values=nb_bankrupt.values))
    fig.update_layout(title="Repartition of bankrupt companies per year", 
    legend={'xanchor':'left','yanchor':'top', 'orientation':'h'})

    context['pie'] = plot(fig, output_type='div')

    # Array
    context['tab'] = udata.head(100).to_html(classes='table table-striped text-center', justify='center')
    
    # ViolinPlot
    if  req.GET.get('violin'):
        v =  req.GET['violin']
        if not v in data.columns:
            v = 'X4'
        else: 
            context['v'] = v
    else:
        v = 'X2'
    context['butterfly'] = plot(px.violin(title='Density of a variable',
        data_frame=data, y=v, x='year', labels={v:desc[v]}), 
        output_type='div')
    
    # ScatterPlot
    if req.GET.get('scatter1') and req.GET.get('scatter2'): 
        v1, v2 = req.GET['scatter1'], req.GET['scatter2']
        if not v1 in data.columns or not v2 in data.columns:
            v1, v2 = 'X1', 'X2'
        else:
            context['v1'] = v1
            context['v2'] = v2
    else:
        v1, v2 = 'X1', 'X2'

    context['scatter'] = plot(
        px.scatter(title='With only 2 variables',
            data_frame=data, x=v1, y=v2, labels={v1:desc[v1], v2:desc[v2]},
            color=['bankrput' if int(x) == 1 else 'not bankrupt' for x in data.X65]
        ), output_type='div')
    
    # BarPlot
    context['bar'] = plot(px.bar(title='Total number of companies',
        y=data.value_counts('year').index, 
        x=data.value_counts('year').values, orientation='h'
    ), output_type='div')

    context['options'] = data.columns

    return render(req, 'core/viz.html', context=context)


def predict(req):
    context = {}
    if req.POST:
        year = req.POST['year']
        opt = int(req.POST['options_input2']), int(req.POST['options_input3'])
        if req.POST['options_input1'] == "csv":
            file = req.FILES['file']
            fs = FileSystemStorage()
            filename = fs.save(file.name, file)
            context['prediction'] = model_prediction(file=filename, year=year, opt=opt[0])
        if req.POST['options_input1'] == "entry":
            entry = req.POST['entry']
            context['prediction'] = model_prediction(entry=entry, year=year, opt=opt[0])

    return render(req, 'core/index.html', context=context)


def model_prediction(file=None, entry=None, year=None, opt=None):
    # Preprocessing
    if file:
        data = pd.read_csv('.' + settings.MEDIA_URL + file)
        data['year'] = year
        data = data.head(10)
    elif entry:
        data = pd.DataFrame([year] + entry.split(',')).T
        data.columns = ['year'] + [f'X{i}' for i in range(1,65)]
    
    data = data_preparation(data, option=opt)
    # TODO scaling
    # scaler = pickle.load('../static/model/scaler.pk')
    # if opt == 1
    # scaler.transform(data)

    # model importation


    return data.to_html(classes='table table-striped text-center', justify='center')