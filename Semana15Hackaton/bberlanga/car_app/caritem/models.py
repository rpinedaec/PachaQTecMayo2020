from django.db import models
from carbrand.models import Brand
from cartype.models import CarType
from carmodel.models import CarModel

class CarItem(models.Model):
    id_brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    id_type = models.ForeignKey(CarType, on_delete=models.CASCADE)
    id_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    year = models.IntegerField()

