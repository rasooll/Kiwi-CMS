from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    """
    This model use for User profile.
    """

    user = models.OneToOneField(
        User,
        verbose_name = "کاربر",
        on_delete = models.CASCADE
    )
    phone = models.CharField(
        verbose_name = "شماره تلفن",
        max_length = 15
    )

    def get_username(self):
        return self.user.username
    get_username.short_description = 'نام کاربری'

    def get_full_name(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)
    get_full_name.short_description = ' نام و نام خانوادگی'

    def __str__(self):
        return self.user.username