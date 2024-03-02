from django.contrib import admin
from .models import Blog

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'update_date', 'create_date')
    list_filter = ('status', 'update_date', 'create_date')
    list_editable = ['status']

    search_fields = ['title']

admin.site.register(Blog, BlogAdmin)
    