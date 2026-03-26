from django.db import models
from location.models import Location
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True, blank=True)
    location=models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    phone=models.CharField(max_length=8,null=True, blank=True,unique=True)
    status = models.CharField(max_length=20, default='beginner',null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.phone}"

