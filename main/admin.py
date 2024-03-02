from django.contrib import admin
from .models import Website_settings, Homepage, Socialmedia, About, Skills, Education, Experience, Works
# Register your models here.

admin.site.register(Website_settings)
admin.site.register(Homepage)
admin.site.register(Socialmedia)
admin.site.register(About)
admin.site.register(Skills)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Works)