from django.db import models

# Create your models here.
class Pelicula(models.Model):
    code = models.CharField( max_length=10)
    name = models.CharField( max_length=50)
    year = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code