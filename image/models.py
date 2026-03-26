from django.db import models

# Create your models here.
class Image(models.Model):
    id=models.BigAutoField(primary_key=True)
    file = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f"{self.file}"