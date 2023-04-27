
from .views import *
from django.urls import path

urlpatterns = [
    path('youtube/', you_tube, name="youtube"),
]
