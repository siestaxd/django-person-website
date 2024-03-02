from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('works/', views.works, name='works'),
    path('contact/', views.contact, name="contact")
] 