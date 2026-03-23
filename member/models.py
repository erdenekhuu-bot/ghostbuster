from django.db import models
from location.models import Location

# Create your models here.
class Member(models.Model):
    id=models.BigAutoField(primary_key=True)
    nickname=models.CharField(max_length=20)
    status=models.CharField(default='beginner')
    location_id=models.ForeignKey(Location,on_delete=models.CASCADE)
    age=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
