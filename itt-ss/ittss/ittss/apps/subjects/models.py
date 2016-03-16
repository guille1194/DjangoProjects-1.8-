from django.db import models

class Subject(models.Model):
	name = models.CharField(max_length = 100, null = True, blank = True)
	content = models.TextField(null = True, blank = True)

	def __unicode__(self):
		return self.name
