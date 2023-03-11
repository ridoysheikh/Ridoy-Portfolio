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
@login_required
def site_info(request):
    if request.method == "POST":
        try:
            navs_item = navs.objects.get(pk=1)
        except:
            navs.objects.create(id=1)
            navs_item = navs.objects.get(pk=1)
        navs_item.nv_title=request.POST.get("title")
        navs_item.seo_title=request.POST.get("seo_title")
        navs_item.seo_description=request.POST.get("Description")
        navs_item.seo_keys=request.POST.get("Tags")
        if request.FILES.get("image"):
            navs_item.nv_logo=request.FILES.get("image")
        navs_item.save()
    try:
        navs_item = navs.objects.get(pk=1)
    except:
        navs.objects.create(id=1)
        navs_item = navs.objects.get(pk=1)
    return render(request, "dashboard/siteInfo.html", {'title': "Change Info's",'section':'settings','navs': navs_item})
@login_required
def smtp_settings(request):
    if request.method == "POST":
        try:
            smtp_sets = smtp.objects.get(pk=1)
        except:
            smtp.objects.create(id=1)
            smtp_sets = smtp.objects.get(pk=1)
        smtp_sets.server=request.POST.get("server")
        smtp_sets.port=request.POST.get("port")
        smtp_sets.username=request.POST.get("username")
        smtp_sets.password=request.POST.get("password")
        smtp_sets.receiver_mail=request.POST.get("receiver_mail")
        smtp_sets.save()
    try:
        smtp_sets = smtp.objects.get(pk=1)
    except:
        smtp.objects.create(id=1)
        smtp_sets = smtp.objects.get(pk=1)
    return render(request, "dashboard/smtp.html", {'title': "Change SMTP's",'section':'settings','smtp': smtp_sets})

@login_required
def contact(request):
    if request.method == "POST":
        
        try:
            contact = contact_info.objects.get(pk=1)
        except:
            contact_info.objects.create(id=1)
            contact = contact_info.objects.get(pk=1)
        contact.title=request.POST.get("title")
        contact.adresses=request.POST.get("adresses")
        contact.phone=request.POST.get("phone")
        contact.email=request.POST.get("email")
        contact.website=request.POST.get("website")
        
        contact.save()
    try:
        contact = contact_info.objects.get(pk=1)
    except:
        contact_info.objects.create(id=1)
        contact = contact_info.objects.get(pk=1)
    return render(request, "dashboard/contact.html", {'title': "Change Addresses",'section':'front','contact': contact})

@login_required
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
        if request.POST.get("marname"):
            social=market(name=request.POST.get("marname"),links=request.POST.get("marlinks"),logo_img=request.FILES.get("marlogo_img"))
            social.save()
        
    bg_img=bg_images.objects.all()
    social=social_id.objects.all()
    profs=profession.objects.all()
    markets=market.objects.all()
    return render(request, "dashboard/Edit_home.html", {'title': "Change Home Pages",'section':'front','prof':profs,"sid":social,'bg_image':bg_img,'markets':markets})

@login_required
def del_prof(request, id):
    profs=profs=profession.objects.get(pk=id)
    profs.delete()
    return redirect('home_set')

@login_required
def del_social(request, id):
    social=social_id.objects.get(pk=id)
    social.delete()
    return redirect('home_set')

def del_mar(request, id):
    obj=market.objects.get(pk=id)
    obj.delete()
    return redirect('home_set')


@login_required
def del_bg(request, id):
    social=bg_images.objects.get(pk=id)
    social.delete()
    return redirect('home_set')

@login_required
def resumes_edit(request):
    if request.method == "POST":
        pass
    education = educations.objects.prefetch_related('catagory')
    skils = skills.objects.prefetch_related('catagory')
    return render(request, "dashboard/resume_d.html", {'title': "Change Resume's",'section':'front','education':education,'skils':skils})

@login_required
def add_edu(request):
    if request.method =="POST":
        if request.POST.get("catname"):
            edu=edu_cat(name=request.POST.get("catname"))
            edu.save()
        if request.POST.get("title"):
            education=educations(title=request.POST.get("title"),institute=request.POST.get("institute"),start_year=request.POST.get("start_year"),end_year=request.POST.get("end_year"),description=request.POST.get("description"),catagory=edu_cat.objects.get(pk=request.POST.get("catagory")))
            education.save()
            return redirect('resumes_edit')
    edu=edu_cat.objects.all()
    return render(request, "dashboard/educations.html", {'title': "Add Educations",'section':'front',"edu":edu})

@login_required
def educatdel(request, id):
    obj=edu_cat.objects.get(pk=id)
    obj.delete()
    return redirect('add_edu')
@login_required
def edudel(request, id):
    obj=educations.objects.get(pk=id)
    obj.delete()
    return redirect('resumes_edit')

@login_required
def eduedit(request,id):
    if request.method == "POST":
        edu=educations.objects.get(pk=id)
        edu.title=request.POST.get("title")
        edu.institute=request.POST.get("institute")
        edu.start_year=request.POST.get("start_year")
        edu.end_year=request.POST.get("end_year")
        edu.description=request.POST.get("description")
        edu.save()
        return redirect('resumes_edit')
    edu=educations.objects.get(pk=id)
    return render(request, "dashboard/educations_edit.html", {'title': "Edit Educations",'section':'front','edu':edu})



@login_required
def add_skils(request):
    if request.method =="POST":
        if request.POST.get("Skillname"):
            Skill=Skill_cat(name=request.POST.get("Skillname"))
            Skill.save()
        if request.POST.get("title"):
            obj=skills(title=request.POST.get("title"),proggress=request.POST.get("proggress"),catagory=Skill_cat.objects.get(pk=request.POST.get("catagory")))
            obj.save()
            return redirect('resumes_edit')
    Skill=Skill_cat.objects.all()
    return render(request, "dashboard/skils.html", {'title': "Add Skils",'section':'front',"Skill":Skill})

@login_required
def skilscatdel(request, id):
    obj=Skill_cat.objects.get(pk=id)
    obj.delete()
    return redirect('add_skils')
@login_required
def skilsdel(request, id):
    obj=skills.objects.get(pk=id)
    obj.delete()
    return redirect('resumes_edit')