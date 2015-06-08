from django.db import models

class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"
    
    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32)
    content = models.TextField()
    
    def __str__(self):
        return self.title