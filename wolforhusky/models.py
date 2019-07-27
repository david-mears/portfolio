from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models

from io import BytesIO
import PIL
from PIL import ImageOps
import sys

class Image(models.Model):
    image = models.ImageField(upload_to='images/')

    def save(self, force_insert=False, force_update=False):
        
        super(Image, self).save(force_insert, force_update)

        img = PIL.Image.open(self.image.path)
        img = ImageOps.fit(img, (224, 224), PIL.Image.ANTIALIAS)
        img.save(self.image.path)