from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    class Meta:
        verbose_name= 'Profile'
        verbose_name_plural = 'Profile'

    LEVEL = (
        ('n', 'Newbie Hacker'),
        ('j', 'Junior Hacker'),
        ('s', 'Senior Hacker'),
        ('p', 'Professional Hacker'),
        ('w', 'World Class Hacker'),
        ('g', 'GOD Hacker'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nick = models.CharField(max_length=50, blank=True,)

    birth_date = models.DateField(null=True)
    intro = models.TextField(blank=True,help_text='Introduce your self.')

    profile_image = models.ImageField(blank=True, upload_to='user/profile_pic')
    level = models.CharField(
        max_length=1,
        choices=LEVEL,
        blank = True,
        default='n',
        help_text='Class Level',
    )
