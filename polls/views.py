from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

# Create your views here.

def HomePageView(request):
    return HttpResponse(f"<h1>This is homepage for polls app!</h1>")