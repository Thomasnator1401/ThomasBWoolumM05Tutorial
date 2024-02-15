# gunicorn_django.py
from gunicorn.app.wsgiapp import WSGIApplication

application = WSGIApplication("%(proj_name)s.wsgi:application")

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('articles/<int:year>/', views.year_archive),
]

# views.py
from django.http import HttpResponse
from django.shortcuts import render

def hello_world(request):
    return HttpResponse("Hello, World!")

# models.py
from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name
