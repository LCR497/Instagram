from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    avatar = models.ImageField()
    password = models.CharField()
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    followers = models.IntegerField()
    follow = models.IntegerField()
    
class Post(models.Model):
    author = models.ForeignKey(User.name)
    title = models.CharField(max_length=50)
    image = models.ImageField()
    description = models.TextField()
    likes = models.BooleanField(default=False)