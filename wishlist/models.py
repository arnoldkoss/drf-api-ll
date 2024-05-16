from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Wishlist(models.Model):
    """
    Wishlist model with a foreign key to user.
    Allows users to save posts to their personal wishlist.
    Each entry in the wishlist links a user to a post they have marked.
    """
    owner = models.ForeignKey(
        User, related_name='wishlist', on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post, related_name='wishlist', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{self.owner} {self.post}'
