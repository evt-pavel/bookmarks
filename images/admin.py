from django.contrib import admin
from .models import Image

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_disolay = ['title', 'slug', 'images', 'created']
    list_filter = ['created']

# Register your models here.
