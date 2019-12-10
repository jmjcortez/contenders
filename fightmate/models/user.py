from django.db import models
# from django.db import get_models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from fightmate.managers.user import UserManager
from fightmate.models.location import City, Country
from fightmate.models.discipline import UserDiscipline

class User(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(unique=True)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100, null=True, blank=True)
	date_of_birth = models.DateTimeField(null=True, blank=True)
	weight = models.FloatField(null=True, blank=True)
	height = models.FloatField(null=True, blank=True)
	city = models.CharField(max_length=100, null=True, blank=True)
	country = models.CharField(max_length=100, null=True, blank=True)

	gender = models.CharField(max_length=100, null=True, blank=True)
	nationality = models.CharField(max_length=100, null=True, blank=True)

	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)

	city = models.ForeignKey(City, on_delete=models.PROTECT, null=True)
	country = models.ForeignKey(Country, on_delete=models.PROTECT, null=True)

	objects = UserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name']

	def get_latest_bio(self):
		return self.bios.filter(is_last=True).first()
	
	def get_disciplines(self):
		user_disciplines = UserDiscipline.objects.select_related('discipline').filter(user=self)
		return [ user_discipline.discipline for user_discipline in user_disciplines ]
	
	def get_pkg(self):
		user_disciplines = UserDiscipline.objects.select_related('discipline').filter(user=self)

		pkg = {
			'punch': user_disciplines.filter(discipline__punch=True).exists(),
			'kick': user_disciplines.filter(discipline__kick=True).exists(),
			'grapple': user_disciplines.filter(discipline__grapple=True).exists()
		}

		return pkg