
from .views import *
from django.urls import path

urlpatterns = [
    path('video/downloader/', you_tube, name="videodonloader"),
]
