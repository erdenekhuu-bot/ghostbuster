from django.db import models
from location.models import Location

# Create your models here.
class Member(models.Model):
    id=models.BigAutoField(primary_key=True)
    nickname=models.CharField(max_length=20,blank=True, null=True)
    status=models.CharField(default='beginner',blank=True, null=True)
    location_id=models.ForeignKey(Location,on_delete=models.CASCADE)
    age=models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
