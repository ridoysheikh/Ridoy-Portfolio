from django.shortcuts import render, redirect
from Front_Pages.models import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime,math
from django.http import HttpResponse
from django.db.models import Q
import datetime
from xml.etree import ElementTree as ET
from PIL import Image, ExifTags
from io import BytesIO
from django.core.files import File


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
            uploaded_image = request.FILES.get("image")

            # Resize the image
            new_size = (200, 200)
            image = Image.open(uploaded_image)
            image = image.resize(new_size)

            # Save the resized image to the model
            img_io = BytesIO()
            image.save(img_io, format='png')  # You can change the format if needed
            navs_item.nv_logo.save(uploaded_image.name, File(img_io), save=False)


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

def fix_image_orientation(image):
    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break
        exif = dict(image._getexif().items())

        if exif[orientation] == 3:
            image = image.rotate(180, expand=True)
        elif exif[orientation] == 6:
            image = image.rotate(270, expand=True)
        elif exif[orientation] == 8:
            image = image.rotate(90, expand=True)

    except (AttributeError, KeyError, IndexError):
        # No EXIF data found or the image doesn't need rotation
        pass

    return image
@login_required
def home_set(request):
    if request.method == "POST":
        if request.POST.get("pname"):
            profs=profession(name=request.POST.get("pname"))
            profs.save()
        if request.POST.get("links"):
            if request.FILES.get("logo_img"):
                social=social_id(name=request.POST.get("name"),links=request.POST.get("links"))
                uploaded_image = request.FILES.get("logo_img")
                # Resize the image
                new_size = (50, 50)
                image = Image.open(uploaded_image)
                image = image.resize(new_size)

                # Save the resized image to the model
                img_io = BytesIO()
                image.save(img_io, format='png')  # You can change the format if needed
                social.logo_img.save(uploaded_image.name, File(img_io), save=False)
                social.save()
            else:
                social=social_id(name=request.POST.get("name"),links=request.POST.get("links"))
                social.save()
        if request.POST.get("bg_mode"):
            bg_img=bg_images(bg_mode=request.POST.get("bg_mode"))
            uploaded_image = request.FILES.get("bg_image")
            # Resize the image

            if request.POST.get("bg_mode") == "Portrait":
                new_size = (480, 798)
            else:
                new_size = (1024, 768)
            
            image = Image.open(uploaded_image)
            image = fix_image_orientation(image)
            image = image.resize(new_size)
            # Save the resized image to the model
            img_io = BytesIO()
            image.save(img_io, format='png')  # You can change the format if needed
            bg_img.bg_image.save(uploaded_image.name, File(img_io), save=False)
            
            bg_img.save()
        if request.POST.get("marname"):
            if request.FILES.get("marlogo_img"):
                social=market(name=request.POST.get("marname"),links=request.POST.get("marlinks"))
                uploaded_image = request.FILES.get("marlogo_img")
                # Resize the image
                new_size = (50, 50)
                image = Image.open(uploaded_image)
                image = image.resize(new_size)
                # Save the resized image to the model
                img_io = BytesIO()
                image.save(img_io, format='png')  # You can change the format if needed
                social.logo_img.save(uploaded_image.name, File(img_io), save=False)
                social.save()
            else:
                social=market(name=request.POST.get("marname"),links=request.POST.get("marlinks"))
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
def contract(request, page):
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
        # if request.GET.get('method') == "remove":
        #     id=request.GET.get('id')
        #     cont=contacts.objects.get(pk=id)
        #     print("a")
        #     cont.delete()
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
            request.POST=None
            cont.save()
            return redirect("contract",page=page)
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
            return redirect("contract",page=page)

    except Exception as e:
        return HttpResponse(f"Error {e}")
    
    try:
        if page:
            page = int(page)
        else:
            page=1
        start_item = (page-1)*10
        if request.GET.get('search_query'):
            search_query=request.GET.get('search_query')
            cont = contacts.objects.filter(Q(name__icontains=search_query) | Q(address__icontains=search_query) | Q(reletion__icontains=search_query) | Q(phone_number__icontains=search_query) | Q(email__icontains=search_query))
        else:
            cont = contacts.objects.all()
        max_page=math.floor((len(cont)-1)/10)
        if len(cont) > start_item and len(cont) <= start_item+10:
                cont=cont[start_item:]
        elif len(cont) > start_item:
                cont=cont[start_item:start_item+10]
        elif len(cont) < start_item:
            return HttpResponse("<h1>not result Found</h1>")
        else:
            cont=cont
    except Exception as e:
        return HttpResponse(e)
    return render(request, "dashboard/contract.html", {'title': "View Contacts",'section':'contact','contract':cont,'pages':page,'mpage':max_page+1,'ppage':page-1,'npage':page+1})

def get_sitemap_xml(request):
    urls=['https://devridoy.com/',
    'https://devridoy.com/resume/',
    'https://devridoy.com/contact/',
    'https://devridoy.com/video/downloader/',
    'https://devridoy.com/pdf/'
    ]
    urlsetstart='<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    urlsetend="</urlset>"
    url=""
    for u in urls:
        url+= "\n<url>\n  <loc>"+str(u)+"</loc>\n<lastmod>"+str(datetime.date.today())+"</lastmod>\n<changefreq>always</changefreq>\n<priority>1.0</priority>\n</url>"
    
    resp=urlsetstart+"\n"+url+"\n"+urlsetend
    
    return HttpResponse(resp ,content_type='text/xml')

