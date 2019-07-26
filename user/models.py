from django.db import models
from django.contrib.auth.models import AbstractUser, Group

# Create your models here.


class User(AbstractUser):
    email = models.CharField(max_length=150, unique=True)
    groups = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)

    REQUIRED_FIELDS = ['groups_id', 'email']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.username
