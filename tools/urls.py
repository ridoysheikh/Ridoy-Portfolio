
from .views import *
from django.urls import path

urlpatterns = [
    path('video/downloader/', you_tube, name="videodonloader"),
    path('pdf/', pdf_tool, name="pdf_tool"),
]
