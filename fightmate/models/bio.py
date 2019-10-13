from django.db import models


class Bio(models.Model):
	user = models.ForeignKey('User', on_delete=models.PROTECT) #related name
	time_state = models.DateTimeField()
	text = models.TextField(blank=True)
	is_last = models.BooleanField()

	class Meta:
		db_table = 'bio'
