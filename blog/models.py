from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from djmoney.models.fields import MoneyField

TYPE = (
    (0,"Full-time"),
    (1,"Part-time"),
    (2,"Intern"),
)


class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Careers(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    salary = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    content = RichTextField()
    created_on = models.DateTimeField(auto_now_add=True)
    type = models.IntegerField(choices=TYPE, default=0)
    category = models.ForeignKey(Category, on_delete= models.CASCADE, null=True)
    tags = models.ManyToManyField('Tag')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name