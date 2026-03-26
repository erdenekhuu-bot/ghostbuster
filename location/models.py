from django.db import models
from video.models import Video
from image.models import Image

# Create your models here.
class Location(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(default='',null=True,blank=True,max_length=255,unique=True)
    description=models.CharField(default='',null=True,blank=True,max_length=800)
    address=models.CharField(default='',null=True,blank=True)
    image=models.ForeignKey(Image,on_delete=models.CASCADE,null=True,blank=True)
    video=models.ForeignKey(Video, on_delete=models.CASCADE,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.address}"
    