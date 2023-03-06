from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Prefetch
from .models import *
import smtplib


def api(request):
    if request.method == 'GET':
        if request.GET.get('name') == "bgimage" and request.GET.get('screen') == "Portrait":
            scr_size=request.GET.get('screen')
            images = bg_images.objects.filter(bg_mode=scr_size).values_list('bg_image', flat=True)
            images=list(images)
            return JsonResponse({'images':images})
        elif request.GET.get('name') == "bgimage" and request.GET.get('screen') == "Landscape":
            scr_size=request.GET.get('screen')
            images = bg_images.objects.filter(bg_mode=scr_size).values_list('bg_image', flat=True)
            images=list(images)
            return JsonResponse({'images':images})
        elif request.GET.get('name') == "profession":
            text=profession.objects.values_list('name', flat=True)
            text=list(text)
            return JsonResponse({'text':text})

def home(request):
    title = "Home"
    navs_item = navs.objects.get(pk=1)
    social=social_id.objects.all()
    return render(request, 'front/home.html',context={'title': title, 'navs': navs_item, 'social':social})

def resumes(request):
    title = "Resume"
    navs_item = navs.objects.get(pk=1)
    edu = edu_cat.objects.all().prefetch_related(Prefetch('educations_set', queryset=educations.objects.all().order_by('-start_year')))
    skill = Skill_cat.objects.all().prefetch_related(Prefetch('skills_set', queryset=skills.objects.all()))
    return render(request, 'front/resume.html',context={'title': title, 'navs': navs_item, 'edu':edu, 'skill': skill})

def contact(request):
    title = "Hire Me"
    navs_item = navs.objects.get(pk=1)
    contacts=contact_info.objects.get(pk=1)
    if request.method == "POST":
        # get form submitions
        name = request.POST.get('name')
        email = request.POST.get('email')
        messages = request.POST.get('message')
        Email_body = f'From: {name} ({email}) \n {messages}'
        # Get smtp data
        smtps=smtp.objects.get(pk=1)
        # Set up the SMTP connection
        smtp_server = smtps.server
        smtp_port = smtps.port
        smtp_username = smtps.username
        smtp_password = smtps.password
        sender_email = email
        recipient_email = smtps.receiver_mail
        email_subject = f"{name} Is Messaged You"
        # Create an SMTP object
        smtp_obj = smtplib.SMTP(smtp_server, smtp_port)
        # Start the SMTP server connection
        smtp_obj.starttls()
        # Log in to the SMTP server
        smtp_obj.login(smtp_username, smtp_password)
        # Send the email message
        message = f"Subject: {email_subject}\n\n{Email_body}"
        smtp_obj.sendmail(sender_email, recipient_email, message)
        smtp_obj.quit()
        return render(request, 'front/contact.html',context={'title': title, 'navs': navs_item, 'contacts':contacts,'success': True})

    return render(request, 'front/contact.html',context={'title': title, 'navs': navs_item, 'contacts':contacts})