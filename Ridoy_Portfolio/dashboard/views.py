from django.shortcuts import render, redirect
from Front_Pages.models import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def log_in(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            pass
    return render(request, "dashboard/login.html",{})

@login_required()
def Logout(request):
    logout(request)
    return redirect('dashboard')
@login_required
def dashboard(request):
    return render(request, "dashboard/dashboard.html", {'title': "Dashboard",})

def site_info(request):
    if request.method == "POST":
        navs_item = navs.objects.get(pk=1)
        navs_item.nv_title=request.POST.get("title")
        navs_item.seo_title=request.POST.get("seo_title")
        navs_item.seo_description=request.POST.get("Description")
        navs_item.seo_keys=request.POST.get("Tags")
        if request.FILES.get("image"):
            navs_item.nv_logo=request.FILES.get("image")
        navs_item.save()
    navs_item = navs.objects.get(pk=1)
    return render(request, "dashboard/siteInfo.html", {'title': "Change Info's",'section':'settings','navs': navs_item})

def smtp_settings(request):
    if request.method == "POST":
        smtp_sets = smtp.objects.get(pk=1)
        smtp_sets.server=request.POST.get("server")
        smtp_sets.port=request.POST.get("port")
        smtp_sets.username=request.POST.get("username")
        smtp_sets.password=request.POST.get("password")
        smtp_sets.receiver_mail=request.POST.get("receiver_mail")
        smtp_sets.save()
    smtp_sets = smtp.objects.get(pk=1)
    return render(request, "dashboard/smtp.html", {'title': "Change SMTP's",'section':'settings','smtp': smtp_sets})

def contact(request):
    if request.method == "POST":
        contact = contact_info.objects.get(pk=1)
        contact.title=request.POST.get("title")
        contact.adresses=request.POST.get("adresses")
        contact.phone=request.POST.get("phone")
        contact.email=request.POST.get("email")
        contact.website=request.POST.get("website")
        
        contact.save()
    contact = contact_info.objects.get(pk=1)
    return render(request, "dashboard/contact.html", {'title': "Change Addresses",'section':'front','contact': contact})

def home_set(request):
    if request.method == "POST":
        if request.POST.get("pname"):
            profs=profession(name=request.POST.get("pname"))
            profs.save()
        if request.POST.get("links"):
            social=social_id(name=request.POST.get("name"),links=request.POST.get("links"),logo_img=request.FILES.get("logo_img"))
            social.save()
        if request.POST.get("bg_mode"):
            bg_img=bg_images(bg_mode=request.POST.get("bg_mode"),bg_image=request.FILES.get("bg_image"))
            bg_img.save()
    bg_img=bg_images.objects.all()
    social=social_id.objects.all()
    profs=profession.objects.all()
    return render(request, "dashboard/Edit_home.html", {'title': "Change Home Pages",'section':'front','prof':profs,"sid":social,'bg_image':bg_img})

def del_prof(request, id):
    profs=profs=profession.objects.get(pk=id)
    profs.delete()
    return redirect('home_set')

def del_social(request, id):
    social=social_id.objects.get(pk=id)
    social.delete()
    return redirect('home_set')

def del_bg(request, id):
    social=bg_images.objects.get(pk=id)
    social.delete()
    return redirect('home_set')


