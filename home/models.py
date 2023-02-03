from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class Team(models.Model):

    img = models.ImageField(upload_to='team')
    name = models.CharField(max_length=200)
    job = models.CharField(max_length=200, default='Developer')
    linkedin = models.CharField(max_length=500, null=True, blank=True)
    github = models.CharField(max_length=500, null=True, blank=True)
    twitter = models.CharField(max_length=500, null=True, blank=True)
    facebook = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self) -> str:
        return self.name