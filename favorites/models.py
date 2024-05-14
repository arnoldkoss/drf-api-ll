from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Favorite(models.Model):
    """
    Favorite model to allow users to save their 
    favorite posts.
    Each favorite links a user to a post  they have marked as favorite.
    """
    owner = models.ForeignKey(
        User, related_name='favorites', on_delete=models.CASCADE)
    
    post = models.ForeignKey(
        Post, related_name='favorites', on_delete=models.CASCADE, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created_at']
        unique_together = ('owner', 'post')

    
    def __str__(self):
        return f'{self.owner} {self.post}'


    
