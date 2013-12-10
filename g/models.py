from django.db import models

# Create your models here.

class Gallery(models.Model):
	name = models.CharField(max_length=200, null=False, unique=True)
	date = models.DateField()
	description = models.CharField(max_length=10240)

	def __unicode__(self):
		return self.name
	class Meta:
		db_table = 'gallery'

class Photo(models.Model):
	path = models.CharField(max_length=1024, null=False)
	description = models.CharField(max_length=10240)
	gallery = models.ForeignKey(Gallery)
	labels = models.CharField(max_length=1024)
	type = models.CharField(max_length=200)

	def __unicode__(self):
		return self.path
	class Meta:
		db_table = 'photo'

class Topic(models.Model):
	name = models.CharField(max_length=200, null=False, unique=True)
	photos = models.ManyToManyField(Photo)
	descripton = models.CharField(max_length=10240)

	def __unicode(self):
		return self.name
	class Meta:
		db_table = 'topic'

class Slide(models.Model):
	name = models.CharField(max_length=200, null=False, unique=True)
	function = models.CharField(max_length=200)

	def __unicode__(self):
		return self.name
	class Meta:
		db_table = 'slide'
