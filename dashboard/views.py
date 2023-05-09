from django.shortcuts import render, redirect
from Front_Pages.models import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponse


def log_in(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        email=request.POST.get("email")
        password=request.POST.get("password")
        user = authenticate(request, email=email, password=password)
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
    return render(request, "dashboard/siteInfo.html", {'title': "Change Info's",'section':'siteinf','navs': navs_item})
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
    return render(request, "dashboard/smtp.html", {'title': "Change SMTP's",'section':'smtp','smtp': smtp_sets})

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
    return render(request, "dashboard/contact.html", {'title': "Change Addresses",'section':'cont','contact': contact})

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
    return render(request, "dashboard/Edit_home.html", {'title': "Change Home Pages",'section':'home','prof':profs,"sid":social,'bg_image':bg_img,'markets':markets})

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
    return render(request, "dashboard/resume_d.html", {'title': "Change Resume's",'section':'resum','education':education,'skils':skils})

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
    return render(request, "dashboard/educations.html", {'title': "Add Educations",'section':'resum',"edu":edu})

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
    return render(request, "dashboard/educations_edit.html", {'title': "Edit Educations",'section':'resum','edu':edu})



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
    return render(request, "dashboard/skils.html", {'title': "Add Skils",'section':'resum',"Skill":Skill})

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
@login_required()
def contract(request):
    try:
        if request.GET.get('method') == "connected":
            id=request.GET.get('id')
            cont=contacts.objects.get(pk=id)
            cont.last_contacted=datetime.date.today()
            cont.save()
            print("c")
        if request.GET.get('method') == "meeted":
            id=request.GET.get('id')
            cont=contacts.objects.get(pk=id)
            cont.last_meet=datetime.date.today()
            cont.save()
            print("b")
        if request.GET.get('method') == "remove":
            id=request.GET.get('id')
            cont=contacts.objects.get(pk=id)
            print("a")
            cont.delete()
        if request.POST.get('name'):
            cont = contacts(
            name=request.POST.get('name'),
            address=request.POST.get('address'),
            reletion=request.POST.get('reletion'),
            phone_number=request.POST.get('phon_num'),
            email=request.POST.get('email'),
            profile_pic=request.FILES.get("file"),
            fb_id=request.POST.get('fbid'),
            last_meet=request.POST.get('last_meet') if request.POST.get('last_meet') else datetime.date.today(),
            DOB=request.POST.get('dob') if request.POST.get('dob') else datetime.date.today(),
            last_contacted=request.POST.get('last_conn') if request.POST.get('last_conn') else datetime.date.today()
            )
            cont.save()
        if request.POST.get('id'):
            cont=contacts.objects.get(pk=request.POST.get('id'))
            cont.name=request.POST.get('nname')
            cont.address=request.POST.get('address')
            cont.reletion=request.POST.get('reletion')
            cont.fb_id=request.POST.get('fbid')
            cont.phone_number=request.POST.get('phon_num')
            cont.email=request.POST.get('email')
            if request.POST.get('dob'):
                cont.DOB=request.POST.get('dob')
            if request.FILES.get("file") !="" and request.FILES.get("file") != None and request.FILES.get("file"):
                cont.profile_pic=request.FILES.get("file")
            cont.save()


    except Exception as e:
        HttpResponse(f"Error {e}")

    cont = contacts.objects.all()
    return render(request, "dashboard/contract.html", {'title': "View Contacts",'section':'contact','contract':cont})
