from django.db import models


class category(models.Model):
    forbaby = models.BooleanField(default=True)
    tablet = models.BooleanField(default=True)
    syrup = models.BooleanField(default=True)
    toiletries = models.BooleanField(default=True)
    vitamins = models.BooleanField(default=True)

class products(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    productType = models.ForeignKey(category, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)
    
    
