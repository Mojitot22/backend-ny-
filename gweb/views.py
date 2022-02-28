from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.
def home(request):
    return render(request, 'gweb/home.html')

def execute(request):
    return render(request, 'gweb/execute.html')

def team(request):
    return render(request, 'gweb/team.html')