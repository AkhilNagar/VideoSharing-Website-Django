
from django.shortcuts import render
from website import models
from .models import Video


# Create your views here.

def homepage(request):
    video= Video.objects.all()
    return render(request,'homepage.html',{"video":video,})

def upload(request):
    if request.method=="POST":
        title= request.POST["title"]
        desc = request.POST['desc']
        thumbnail =  request.FILES['thumbnail']
        video =  request.FILES['video']
        videoobj=Video(user=request.user,title=title,description=desc, thumbnail=thumbnail,video=video)


    return render(request,'upload.html',)

