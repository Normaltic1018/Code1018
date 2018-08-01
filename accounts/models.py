from django.db import models
from django.conf import settings

class Profile(models.Model):
    class Meta:
        verbose_name= 'Profile'
        verbose_name_plural = 'Profile'

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nick = models.CharField(verbose_name='NickName', max_length=50, blank=True,)
