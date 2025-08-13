from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "posts")


    def __str__(self):
            return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    blog = models.TextField(blank=True, null=True)
    profile_picture  = models.ImageFields(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
            return self.title