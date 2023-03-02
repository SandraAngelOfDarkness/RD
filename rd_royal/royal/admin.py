from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from . import models
from .models import About, Video, Foto, Blog, Contact

class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'published_date')

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'published_date')

class FotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'published_date')

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date')
    list_filter = ('created_date', 'update_date')
    search_fields = ('title', 'content')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')

admin.site.register(models.About, AboutAdmin)
admin.site.register(models.Video, VideoAdmin)
admin.site.register(models.Foto, FotoAdmin)
admin.site.register(models.Blog, BlogAdmin)
admin.site.register(models.Contact, ContactAdmin)
