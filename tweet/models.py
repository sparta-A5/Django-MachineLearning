from django.db import models
from django.conf import settings

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to="upload")
    
    def __str__(self):
        return self.title