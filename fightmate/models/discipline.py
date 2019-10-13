from django.db import models


class Discipline(models.Model):
	name = models.CharField(max_length=100)

	class Meta:
		db_table = 'discipline'


class UserDiscipline(models.Model):
	user = models.ForeignKey('User', on_delete=models.PROTECT)
	discipline = models.ForeignKey('Discipline', on_delete=models.PROTECT)
	years_of_experience = models.IntegerField()
	
	class Meta:	
		db_table = 'user_discipline'
