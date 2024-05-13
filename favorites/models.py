from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from detectorists.models import Detectorist

class Favorite(models.Model):
    """
    Favorite model to allow users to save their 
    favorite profiles.
    Each favorite links a user to a post or another user's 
    profile they have marked as favorite.
    """
    owner = models.ForeignKey(
        User, related_name='favorites', on_delete=models.CASCADE)
    
    detectorist = models.ForeignKey(
        Detectorist, related_name='favorited_by_users', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created_at']
        unique_together = ('owner', 'detectorist')

    
    def __str__(self):
        return f'{self.owner} {self.detectorist}'


    
