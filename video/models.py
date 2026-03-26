from django.db import models

# Create your models here.
class Video(models.Model):
    id=models.BigAutoField(primary_key=True)
    file = models.FileField(upload_to='videos/', null=True, blank=True)

    def __str__(self):
        return f"{self.file}"