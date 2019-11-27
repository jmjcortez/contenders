from django.db import models


class Bio(models.Model):
	user = models.ForeignKey('User', on_delete=models.PROTECT, related_name='bios') #related name
	time_state = models.DateTimeField()
	text = models.TextField(blank=True)
	is_last = models.BooleanField()

	class Meta:
		db_table = 'bio'


class Pictures(models.Model):
  is_main = models.BooleanField()
  url = models.CharField(max_length=100)
  bio = models.ForeignKey(Bio, on_delete=models.PROTECT, related_name='pictures')

  class Meta:
    db_table = 'pictures'