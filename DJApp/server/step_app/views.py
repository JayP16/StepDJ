from django.shortcuts import render
from .models import StepUser
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')

def profile(request):
    return render(request,'profile.html')
