from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='images/')
    email = models.CharField(max_length=100)
    bio = models.TextField()
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name


class Articles(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    likes = models.ManyToManyField(User, related_name='blog_posts')
    comment = models.TextField()
    # share a post to social media
    share = models.IntegerField()

    def __str__(self):
        return self.name