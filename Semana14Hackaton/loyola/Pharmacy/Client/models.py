from django.db import models

class status(models.Model):
    active = models.BooleanField(default=True)

class document(models.Model):
    DNI = models.BooleanField(default=False)
    Passport = models.BooleanField(default=False)
    immigrationCard = models.BooleanField(default=False)
    RUC = models.BooleanField(default=False)

class clientInfo(models.Model):
    name = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    phone = models.IntegerField(default=0)
    direccion = models.CharField(max_length=200)
    clientDocument = models.ForeignKey(document, on_delete=models.CASCADE)
    clientStatus = models.ForeignKey(status,on_delete=models.CASCADE)
