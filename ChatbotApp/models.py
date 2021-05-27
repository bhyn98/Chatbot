from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    userID = models.CharField(max_length=20)
    userBigMajor = models.CharField(max_length=20)
    userSmallMajor = models.CharField(max_length=20)
