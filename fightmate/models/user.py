from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from fightmate.managers.user import UserManager


class User(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(unique=True)
	first_name = models.CharField(max_length=100)
	date_of_birth = models.DateTimeField(null=True, blank=True)
	weight = models.FloatField(null=True, blank=True)
	height = models.FloatField(null=True, blank=True)
	city = models.CharField(max_length=100, null=True, blank=True)
	country = models.CharField(max_length=100, null=True, blank=True)

	#might change it to PostGIS
	latitude = models.FloatField(null=True, blank=True)
	longitude = models.FloatField(null=True, blank=True)

	gender = models.CharField(max_length=100, null=True, blank=True)
	nationality = models.CharField(max_length=100, null=True, blank=True)

	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)

	objects = UserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name']
