from django.contrib import admin

# Register your models here.
from g import models

class GalleryAdmin(admin.ModelAdmin):
	pass

class PhotoAdmin(admin.ModelAdmin):
	pass

class TopicAdmin(admin.ModelAdmin):
	pass

class SlideAdmin(admin.ModelAdmin):
	pass

admin.site.register(models.Gallery, GalleryAdmin)
admin.site.register(models.Photo, PhotoAdmin)
admin.site.register(models.Topic, TopicAdmin)
admin.site.register(models.Slide, SlideAdmin)
