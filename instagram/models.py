from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Profile(models.Model):
    name = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, blank=True)
    followers = models.IntegerField(default=0)
    follow = models.IntegerField(default=0)

class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField()
    description = models.TextField(null=True, blank=True)
    likes = models.BooleanField(default=False)