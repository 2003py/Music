from django.contrib import admin
from .models import Music


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ('name', 'poster', 'media_file', 'media_type','lyrics')
# Register your models here.
