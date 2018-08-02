from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    class Meta:
        verbose_name= 'Profile'
        verbose_name_plural = 'Profile'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nick = models.CharField(verbose_name='NickName', max_length=50, blank=True,)
    birth_date = models.DateTimeField(null=True, blank=True)
