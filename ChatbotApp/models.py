from django.db import models


class Users(models.Model):
    userName = models.CharField(max_length=10)
    stdNum = models.CharField(max_length=13)
    userEmail = models.CharField(max_length=30)
    created = models.DateTimeField(auto_created=True)

    class Meta:
        ordering = ['created']