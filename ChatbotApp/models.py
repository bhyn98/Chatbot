from django.db import models


class Users(models.Model):
    userName = models.CharField(max_length=10)
    userID = models.CharField(max_length=13)
    userPW = models.CharField(max_length=20)
    userEmail = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']