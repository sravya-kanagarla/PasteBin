from __future__ import unicode_literals

from django.db import models

# Create your models here.


class data(models.Model):
    title = models.CharField(max_length= 20)
    data = models.CharField(max_length=10000)
    user_id = models.IntegerField(max_length=3,null=1)
    token = models.CharField(max_length=32)