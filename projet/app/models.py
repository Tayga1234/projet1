from contextlib import nullcontext
from django.db import models
from .validator import file_size
# Create your models here.
class Video(models.Model):
    caption=models.CharField(max_length=100)
    video=models.FileField(upload_to="video/%y",validators=[file_size])
    def __str__(self):
        return self.caption