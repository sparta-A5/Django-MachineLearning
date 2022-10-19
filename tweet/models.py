from django.db import models

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to="image")
    
    def __str__(self):
        return self.title