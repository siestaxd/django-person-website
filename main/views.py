from django.shortcuts import render, redirect
from .models import Website_settings, Homepage, About, Works, ContactForm
from django.core.mail import send_mail
from mysite.settings import EMAIL_HOST_USER
from django.contrib import messages
from blog.models import Blog
import requests

# Create your views here.

websitesettings = Website_settings.objects.all()
websitesettings_context = {
    'websitesettings': websitesettings
}

def index(request):
    if websitesettings[0].maintenance == True:
        return render(request, 'pages/maintenance.html', websitesettings_context)
    elif websitesettings[0].maintenance == False:
        context = {
            'blog': Blog.objects.filter(status='published'),
            'home': Homepage.objects.all(),
            'socialmedia': Homepage.objects.get(pk=1).socialmedia.all(),
            'websitesettings': Website_settings.objects.get(),
        }
        return render(request, 'pages/index.html', context)
    
def about(request):
    if websitesettings[0].maintenance == True:
        return render(request, 'pages/maintenance.html', websitesettings_context)
    elif websitesettings[0].maintenance == False:
        about = About.objects.get(pk=1)
        user_skills = about.skills.all()
        user_education = about.education.all()
        user_experience = about.experience.all()
        user_profile_picture = Homepage.objects.get(pk=1).image
        context = {
            'about': about,
            'skills' : user_skills,
            'education': user_education,
            'experience': user_experience,
            'user_profile_picture': user_profile_picture,
            'socialmedia': Homepage.objects.get(pk=1).socialmedia.all(),
            'websitesettings': Website_settings.objects.get(pk=1),
        }
        return render(request, 'pages/about.html', context)

def works(request):
    if websitesettings[0].maintenance == True:
        return render(request, 'pages/maintenance.html', websitesettings_context)
    elif websitesettings[0].maintenance == False:
        work = Works.objects.all()
        repos_info = {}
        headers = {
            "Authorization": f"Bearer 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"  # Burada "YOUR_API_KEY" kısmını kendi API anahtarınızla değiştirmeniz gerekmektedir
        }
        for work in work:
            response = requests.get(f"https://api.github.com/repos/{work.link[19::]}", headers=headers)
            repo_info = response.json()
            repo_info = {
                f"{ work.name }": {
                    "name": work.name,
                    "link": work.link,
                    "image": work.image,
                    "stars" : repo_info["stargazers_count"],
                    "issues": repo_info["open_issues_count"],
                    "fork": repo_info["forks_count"]
                }
            }
            repos_info.update(repo_info)    
        return render(request, 'pages/works.html', context={
            'websitesettings': Website_settings.objects.get(),
            'repos_info': repos_info,
        })

def contact(request):
    if websitesettings[0].maintenance == True:
        return render(request, 'pages/maintenance.html', websitesettings_context)
    elif websitesettings[0].maintenance == False:
        if request.method == 'POST':
            name = request.POST['name']
            mail = request.POST['mail']
            subject = request.POST['subject']
            message = request.POST['message']

            form = ContactForm.objects.create(name=name, mail=mail, subject=subject, message=message)
            form.save()
            send_mail(
                f'İletişim Formu - {subject}',
                f'İsim: {name}\nE-posta: {mail}\nMesaj: {message}',
                f'{EMAIL_HOST_USER}',  # Gönderen adresi
                [f'{websitesettings[0].mail}'],  # Alıcı adresi
                fail_silently=False,
            )
            messages.success(request, "Başarıyla iletiniz gönderildi.")
        return render(request, 'pages/contact.html', {
            'websitesettings': Website_settings.objects.get(),
        })