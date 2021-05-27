from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    img = models.ImageField(upload_to='images')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    query = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
