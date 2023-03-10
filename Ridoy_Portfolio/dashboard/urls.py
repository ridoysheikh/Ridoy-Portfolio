"""Ridoy_Portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from .views import *

urlpatterns = [
    path('login/', log_in,name='login'),
    path('dashboard/', dashboard,name='dashboard'),
    path('logout/', Logout,name='logout'),
    path('settings/sites/infos/', site_info, name="site_info"),
    path('settings/smtp/', smtp_settings, name="smtp"),
    path('settings/contact/', contact, name="contact_set"),
    path('settings/home/', home_set, name="home_set"),
    path('delete/prof/<id>/', del_prof, name="del_prof"),
    path('delete/social/<id>/', del_social, name="del_social"),
    path('delete/bg/<id>/', del_bg, name="del_bg"),
    path('setting/resume/', resumes_edit, name="resumes_edit"),
    path('setting/educations/add', add_edu, name="add_edu"),
    path('setting/educations/cat_del/<id>', educatdel, name="educatdel"),
    path('setting/educations/del/<id>', edudel, name="edudel"),
    path('setting/educations/edit/<id>', eduedit, name="eduedit"),
    path('setting/skils/add', add_skils, name="add_skils"),
    path('setting/skils/cat_del/<id>', skilscatdel, name="skilscatdel"),
    path('setting/skils/del/<id>', skilsdel, name="skilsdel"),

]
