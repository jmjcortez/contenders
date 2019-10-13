from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
	email = models.EmailField()
	first_name = models.CharField(max_length=100)
	date_of_birth = models.DateTimeField()
	weight = models.FloatField()
	height = models.FloatField()
	city = models.CharField(max_length=100)
	country = models.CharField(max_length=100)

	#might change it to PostGIS
	latitude = models.FloatField()
	longitude = models.FloatField()



	gender = models.CharField(max_length=100)
	nationality = models.CharField(max_length=100)

	class Meta:
		db_table = 'user'
