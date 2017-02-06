from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Game(models.Model):
	title = models.CharField(max_length=1000)
	platform = models.CharField(max_length=1000)
	score = models.FloatField(default=0.0)
	genre = models.CharField(max_length=1000)
	editors_choice = models.BooleanField(default=False)
	#, `platform`, `score`, `genre`, `editors_choice`

	def __str__(self):
		return self.title