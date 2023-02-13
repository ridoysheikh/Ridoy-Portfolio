
from .views import *
from django.urls import path

urlpatterns = [
    path('', home,name="home"),
    path('resume/', resumes,name="resume"),
    path('contact/', contact,name="contact"),
]
