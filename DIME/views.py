from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'index.html')


def home(request):
    return render(request,'home.html')
@login_required
def java(request):
    return render(request,'javaexam.html')