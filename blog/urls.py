from django.urls import path, include
from . import views

urlpatterns = [
    path('all-blog/', views.blog, name='all_blogs'),
    path('blog/<slug:slug>', views.blog_details, name="blog_detail"),
    path('search/', views.search, name="search")
] 