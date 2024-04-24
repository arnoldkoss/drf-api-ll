from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    Model to represent the following relationship between users.
    Each instance of this model indicates that the 'owner' user follows the 'followed' user.
    """
    owner = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE
    )
    followed = models.ForeignKey(
        User, related_name='followers', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'followed']

    def __str__(self):
        return f'{self.owner} {self.followed}'