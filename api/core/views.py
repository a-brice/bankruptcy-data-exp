from django.shortcuts import redirect, render, HttpResponse
from django.core.files.storage import FileSystemStorage
import pandas as pd
from django.conf import settings
# Create your views here.

def index(req):
    return render(req, 'core/index.html')

def viz(req):
    return render(req, 'core/viz.html')


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

    return data.to_html()