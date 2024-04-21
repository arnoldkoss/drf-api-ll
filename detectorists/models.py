from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Detectorist(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=60, blank=True)
    content = models.CharField(max_length=250, blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_pic_jgfgzn'
    )
    best_find = models.CharField(max_length=150, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Detectorist: {self.owner}"


def create_detectorist(sender, instance, created, **kwargs):
    if created:
        Detectorist.objects.create(owner=instance)

post_save.connect(create_detectorist, sender=User)