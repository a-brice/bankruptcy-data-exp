from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('visualisation', views.viz, name='viz'),
    path('prediction', views.predict, name='predict'),
]
