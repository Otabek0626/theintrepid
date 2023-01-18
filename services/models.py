from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
class Service(models.Model):
    
    type =models.CharField(max_length = 100)
    name = models.CharField(max_length = 100)
    hero_img = models.ImageField(upload_to = 'sevice/pics')
    desc = models.TextField()
    benefits = ArrayField(
            models.CharField(max_length=100, blank=True),
            size=4,
    )
    solution = ArrayField(
            models.CharField(max_length=100, blank=True),
            size=4,
    )
    
    

    def __str__(self):
        return self.name