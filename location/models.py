from django.db import models
from video.models import Video
from image.models import Image

# Create your models here.
class Location(models.Model):
    id=models.BigAutoField(primary_key=True)
    name=models.CharField(blank=True, null=True)
    description=models.CharField(max_length=500,blank=True,null=True)
    lat=models.CharField(blank=True, null=True)
    lng=models.CharField(blank=True, null=True)
    video_id=models.ForeignKey(Video, on_delete=models.CASCADE)
    image_id=models.ForeignKey(Image,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)