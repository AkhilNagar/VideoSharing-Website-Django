
from django.shortcuts import render
from website import models
from .models import Video


# Create your views here.

def homepage(request):
    video= Video.objects.all()
    return render(request,'homepage.html',{"video":video,})

