from django.shortcuts import redirect, render, HttpResponse
from django.core.files.storage import FileSystemStorage
import pandas as pd
from django.conf import settings
from plotly.offline import plot
import plotly.graph_objs as go
import plotly.express as px

# Create your views here.

def index(req):
    return render(req, 'core/index.html')

def viz(req):
    context = {}
    data = pd.read_csv('./static/data.csv')
    context['total_nb'] = len(data)
    context['line_plot'] = plot([go.Scatter(x=[1,3], y=[3,2])], 
                                output_type='div')
    context['pie'] = plot([go.Pie(labels=['re', 'fd'], values=[2,5])], output_type='div')
    context['tab'] = data.iloc[:25].to_html(classes='table table-striped text-center', justify='center')
    context['butterfly'] = plot(px.violin([1,2,3,2,1,2]), output_type='div')
    context['scatter'] = plot([go.Scatter(x=[3,2,4], y=[5,3,5], mode='markers')], output_type='div')
    context['bar'] = plot(px.bar(y=["1","2"], x=[3,2], orientation='h'), output_type='div')
    return render(req, 'core/viz.html', context=context)


def predict(req):
    context = {}
    if req.POST:
        year = req.POST['year']
        if req.POST['options_input1'] == "csv":
            file = req.FILES['file']
            fs = FileSystemStorage()
            filename = fs.save(file.name, file)
            context['prediction'] = model_prediction(file=filename, year=year)
        if req.POST['options_input1'] == "entry":
            entry = req.POST['entry']
            context['prediction'] = model_prediction(entry=entry, year=year)

    return render(req, 'core/index.html', context=context)


def model_prediction(file=None, entry=None, year=None):
    if file:
        data = pd.read_csv('.' + settings.MEDIA_URL + file)
        data['year'] = year
        data = data.head(10)
    elif entry:
        data = pd.DataFrame([year] + entry.split(',')).T
        data.columns = ['year'] + [f'X{i}' for i in range(1,65)]

    return data.to_html(classes='table table-striped text-center', justify='center')