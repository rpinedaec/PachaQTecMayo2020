from django.db import models

class Customer(models.Model):
    id_number=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    usr_name=models.CharField(max_length=200, null=True)
    usr_password=models.CharField(max_length=200, null=True)
    points=models.IntegerField(default=0)