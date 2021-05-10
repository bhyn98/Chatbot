from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


class UserManager(BaseUserManager):
    def create_user(self, userid, username, useremail, userpw=None):
        if not useremail:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(useremail),
            id=userid,
            pw=userpw,
            name=username,
        )

        user.set_password(userpw)
        user.save(using=self._db)
        return user

    def create_superuser(self, userid, username, useremail, userpw=None):
        user = self.model(
            email=self.normalize_email(useremail),
            id=userid,
            pw=userpw,
            name=username,
        )

        user.set_password(userpw)
        user.save(using=self._db)
        return user


class Users(models.Model):
    userName = models.CharField(max_length=10)
    userID = models.CharField(max_length=13, unique=True)
    userPW = models.CharField(max_length=20)
    userEmail = models.CharField(max_length=30, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
