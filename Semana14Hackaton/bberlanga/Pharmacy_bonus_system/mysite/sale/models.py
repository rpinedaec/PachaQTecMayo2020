from django.db import models
from django.utils.timezone import now

pay_type = ((1,'cash'), (2,'card'), (3,'credit card'))
in_pnt = ((1,'yes'), (0,'no'))


class Sale(models.Model):
    date = models.DateTimeField( default=now, editable=False )
    value = models.DecimalField( max_digits=10, decimal_places=2 )
    taxes = models.DecimalField( max_digits=10, decimal_places=2 )
    total_amount = models.DecimalField( max_digits=10, decimal_places=2 )
    opt_payment = models.CharField( max_length=20, choices=pay_type )
    usr_id = models.CharField( max_length=20 )
    usr_point = models.CharField( max_length=5, choices=in_pnt )
    points = models.DecimalField( max_digits=10, decimal_places=2 )
