from django.db import models

# Create your models here.
class Video(models.Model):
    id=models.BigAutoField(primary_key=True)
    path=models.CharField()