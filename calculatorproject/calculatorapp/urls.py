from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('calculatorapp', views.calculatorapp, name = 'calculatorapp'),
    path('submitquery', views.submitquery, name='submitquery'),
]
