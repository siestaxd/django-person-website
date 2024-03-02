from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import *
from main.models import *
from django.db.models import Q

# Create your views here.

websitesettings = Website_settings.objects.get(),

def blog(request):
    if websitesettings[0].maintenance == True:
        return render(request, 'pages/maintenance.html', {
            'websitesettings': websitesettings,
        })
    elif websitesettings[0].maintenance == False:
        blogs = Blog.objects.filter(status='published')
        return render(request, 'blog/all_blog.html',context = {
            'blog': blogs,
            'websitesettings': Website_settings.objects.get(),
            'user_profile_picture': Homepage.objects.get(pk=1).image,
            'about': About.objects.get(pk=1),
            'socialmedia': Homepage.objects.get(pk=1).socialmedia.all(),
        })
    
def search(request):
    query = request.GET.get('query')
    if query:
        result = Blog.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
        results = [blog.title for blog in result]
    else:
        results = ['']
    return JsonResponse(results, safe=False)

def blog_details(request, slug):
    if websitesettings[0].maintenance == True:
        return render(request,'pages/error503.html',{})
    else:
        # Get the post based on slug a published
        blog = get_object_or_404(Blog, slug=slug, status='published')
        return  render(request, 'blog/blog_details.html', { 
            'blog': blog,
            'websitesettings': Website_settings.objects.get(),
            'user_profile_picture': Homepage.objects.get(pk=1).image,
            'about': About.objects.get(pk=1),
            'socialmedia': Homepage.objects.get(pk=1).socialmedia.all(),
            })