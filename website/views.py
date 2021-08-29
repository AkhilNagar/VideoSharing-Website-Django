
from django.shortcuts import render,redirect
from website import models
from .models import Video


# Create your views here.

def homepage(request):
    video= Video.objects.all()
    return render(request,'homepage.html',{"videos":video})

def upload(request):
    if request.method=="POST":
        title= request.POST["title"]
        desc = request.POST['desc']
        thumbnail =  request.FILES['thumbnail']
        video =  request.FILES['video']
        videoobj=Video(user=request.user,title=title,description=desc, thumbnail=thumbnail,video=video)
        videoobj.save()
        return redirect('homepage')

    return render(request,'upload.html',{})


    return render(request,'upload.html',)

def video(request,pk):
    video = Video.objects.get(pk=pk)
    print(video)
    return render(request,'videoView.html',{'video':video})
