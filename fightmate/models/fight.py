from django.db import models


class Fight(models.Model):
	fighter_1 = models.ForeignKey('User', on_delete=models.PROTECT, related_name='first_fighters')
	fighter_2 = models.ForeignKey('User', on_delete=models.PROTECT, related_name='second_fighters')
	discipline = models.ForeignKey('Discipline', on_delete=models.PROTECT)
	fight_time = models.DateTimeField()
	result_fighter_1 = models.CharField(max_length=100, null=True, blank=True)
	result_fighter_2 = models.CharField(max_length=100, null=True, blank=True)

	#fight_lat and lon POST_GIS
	latitude = models.FloatField()
	longitude = models.FloatField()

	class Meta:
		db_table = 'fight'