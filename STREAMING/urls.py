from django.urls import path

from STREAMING.views import *

urlpatterns = [
    path('', index, name='index'),
    path('catalogo/',  misPelis, name='catalogo')
]