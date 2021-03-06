from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

class Fortune(models.Model):
	user = models.ForeignKey(User, related_name='fortunes')
	content = models.CharField(max_length=50)

	def __str__(self):
		return "Fortune: %s" % self.content

class Picture(models.Model):
	fortune = models.ForeignKey(Fortune, related_name='pictures')
	image = models.ImageField(upload_to='%Y/%m/%d')

	def __str__(self):
		return "Picture: %s" % self.id	