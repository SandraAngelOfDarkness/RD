from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from . import models
from .models import About, Video, Foto, Blog, Contact

class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'published_date')

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'video_file', 'published_date')

    def video_field(self, obj):
        return obj.video.url if obj.video else ''
    video_field.short_description = 'Video'

class FotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image_field', 'published_date')

    def image_field(self, obj):
        return obj.photo.url if obj.photo else ''
    image_field.short_description = 'Photo'

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date')
    list_filter = ['created_date', 'update_date']
    search_fields = ('title', 'content')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')

admin.site.register(models.About, AboutAdmin)
admin.site.register(models.Video, VideoAdmin)
admin.site.register(models.Foto, FotoAdmin)
admin.site.register(models.Blog, BlogAdmin)
admin.site.register(models.Contact, ContactAdmin)
