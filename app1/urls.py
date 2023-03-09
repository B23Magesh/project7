from django.urls import path
from app1.views import *
app_name='something'

urlpatterns=[
    path('Yadav/',Yadav,name='Yadav'),
    path('Yadav1/',Yadav1,name='Yadav1'),
]