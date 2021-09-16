from django.urls import path
from .views import *

urlpatterns = [
    path('', scrap, name='scrap'),
    path('newfile/', newfile, name='newfile'),
]