from django.db import models

from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=100)
    address = models.TextField(max_length=300)
    country = models.CharField(max_length=120)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=50)
    phone = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"

@receiver(post_save,sender=User)
def create_profile(instance,created, **kwargs):
    if created: 
        Profile.objects.create(user=instance)
@receiver(post_save,sender=User)
def save_profile(instance,**kwargs):
    instance.profile.save()
