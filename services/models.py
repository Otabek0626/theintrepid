from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
class Service(models.Model):
    
    name = models.CharField(max_length = 100)
    hero_img = models.ImageField(upload_to = 'sevice/pics', blank=True)
    desc = models.TextField()
  
    
    

    def __str__(self):
        return self.name