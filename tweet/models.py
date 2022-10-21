import os
from tkinter.messagebox import NO
from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from uuid import uuid4

# ImageField 파일 이름 변경
def rename_imagefile_to_uuid(instance, filename):
    upload_to = f'upload/{instance}'
    ext = filename.split('.')[-1]
    uuid = uuid4().hex

    if instance:
        filename = 'cat.jpg'.format(uuid, instance, ext)
    else:
        filename = '{}.{}'.format(uuid, ext)
    
    return os.path.join(upload_to, filename)

# ImageField 파일 이름 덮어쓰기(중복 허용)
class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to=rename_imagefile_to_uuid, max_length=255, storage=OverwriteStorage())
    
    def __str__(self):
        return self.title