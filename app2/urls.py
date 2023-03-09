from django.urls import path
from app2.views import *
app_name='nothing'
urlpatterns = [
    path('Muni/',Muni,name='Muni'),
    path('Muni1/',Muni1,name='Muni1'),
]