from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=200)
    dob = models.DateField(null=True, blank=True)
    cover_pic = models.ImageField(upload_to='uploads', blank=True)
    dp = models.ImageField(upload_to='uploads', blank=True)
    website = models.URLField()
    skills = models.TextField()

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        if instance.profile:
            instance.profile.save()
        else:
            Profile.create_user_profile(sender, instance, True, **kwargs)

    def __str__(self):
        return self.user.username