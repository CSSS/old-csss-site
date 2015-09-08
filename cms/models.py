from django.db import models
from django_markdown.models import MarkdownField

class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"
    
    name = models.CharField(max_length=32,unique=True)
    slug = models.SlugField(max_length=32,unique=True)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=32,unique=True)
    slug = models.SlugField(max_length=32,unique=True)
    content = MarkdownField()
    
    def __str__(self):
        return self.title

class Announcement(models.Model):
    title = models.CharField(max_length=32,unique=True)
    author = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32,unique=True)
    content = models.TextField()
    created = models.DateTimeField()

    def __str__(self):
        return self.title
