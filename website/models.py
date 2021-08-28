from django.db import models

# Create your models here.
class Video(models.Model):
    title=models.CharField(max_length=200,default="")
    description = models.TextField(max_length=1000,default="")
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    date = models.CharField(default="",max_length=100)
    #thumbnail = models.ImageField(upload_to='thumbnail_uploaded',default = None)
    #video = models.FileField(upload_to='videos_uploaded',validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])], default=None)

