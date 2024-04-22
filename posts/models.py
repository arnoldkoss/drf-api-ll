from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Represents a post made by a user in the system. 
    Includes functionality such as image upload and automatic timestamping.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_pic_jgfgzn', blank=True
    )
    location = models.CharField(max_length=50, default="My secret place")
    era = models.CharField(max_length=100, default="Historical era of the find")

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'