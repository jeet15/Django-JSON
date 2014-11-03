from django.db import models
from cars.settings import PHOTO_UPLOAD_DIR

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=120)
    image = models.FileField(upload_to = PHOTO_UPLOAD_DIR)

    def __unicode__(self):
        return self.name
