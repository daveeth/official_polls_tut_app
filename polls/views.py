from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def HomePageView(request):
    return HttpResponse("<h1>This is homepage for polls app!</h1>")