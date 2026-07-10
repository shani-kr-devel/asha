from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'layout.html')

def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request, 'login.html')