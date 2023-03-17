from django.shortcuts import render
from django.http import HttpResponse
from .models import About, Video, Foto, Blog, Contact
from . import models

def index(request):
    return render(request, "royal/index.html", )

def about(request):
    about = models.About.objects.all()
    return render(request, 'royal/about.html', {
        'about': about,
    })

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Contact.objects.create(name=name, email=email, subject=subject, message=message)
    return render(request, 'royal/contact.html')