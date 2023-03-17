from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
from django.contrib.auth.models import User

class About(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/')
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ("Video")

class Foto(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image_field = models.FileField(upload_to='photos/')
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.image_field)
    
    class Meta:
        verbose_name = ("Foto")

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ("Blog")

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = ("Contact")