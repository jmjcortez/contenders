from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'country'

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey('Country', on_delete=models.PROTECT, related_name='cities')

    class Meta:
        db_table = 'city'