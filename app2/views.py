from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Muni(request):
    return HttpResponse('<h2>Super Star Muni</h2>')
def Muni1(request):
    return HttpResponse('<h1><marquee>Super Hero Muni</marquee></h1>')