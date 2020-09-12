from django.db import models


class adminInfo(models.Model):
    name = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
