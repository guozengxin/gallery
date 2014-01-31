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
	name = models.CharField(max_length=128, null=False)
	small_path = models.CharField(max_length=1024)
	middle_path = models.CharField(max_length=1024)
	large_path = models.CharField(max_length=1024)
	description = models.CharField(max_length=10240)
	gallery = models.ForeignKey(Gallery)
	ok = models.BooleanField(default=True)
	labels = models.CharField(max_length=1024)

	def __unicode__(self):
		return self.path
	class Meta:
		db_table = 'photo'

class Topic(models.Model):
	name = models.CharField(max_length=200, null=False, unique=True)
	photos = models.ManyToManyField(Photo)
	description = models.CharField(max_length=10240)

	def __unicode(self):
		return self.name
	class Meta:
		db_table = 'topic'

class Slide(models.Model):
	name = models.CharField(max_length=200, null=False, unique=True)
	function = models.CharField(max_length=200)
	description = models.CharField(max_length=10240)

	def __unicode__(self):
		return self.name
	class Meta:
		db_table = 'slide'
