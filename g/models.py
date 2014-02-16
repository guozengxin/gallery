from django.db import models

# Create your models here.

from datetime import datetime
from time import strftime
#
# Custom field types in here.
#
class UnixTimestampField(models.DateTimeField):
	"""UnixTimestampField: creates a DateTimeField that is represented on the
	database as a TIMESTAMP field rather than the usual DATETIME field.
	"""
	def __init__(self, null=False, blank=False, **kwargs):
		super(UnixTimestampField, self).__init__(**kwargs)
		# default for TIMESTAMP is NOT NULL unlike most fields, so we have to
		# cheat a little:
		self.blank, self.isnull = blank, null
		self.null = True # To prevent the framework from shoving in "not null".

	def db_type(self, connection):
		typ=['TIMESTAMP']
		# See above!
		if self.isnull:
			typ += ['NULL']
		if self.auto_created:
			typ += ['default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP']
		return ' '.join(typ)

	def to_python(self, value):
		return datetime.from_timestamp(value)

	def get_db_prep_value(self, value, connection, prepared=False):
		if value==None:
			return None
		return strftime('%Y%m%d%H%M%S',value.timetuple())

	def to_python(self, value):
		return value

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
	lastmodified = UnixTimestampField(auto_created=True)

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
