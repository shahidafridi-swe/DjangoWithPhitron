from django.contrib import admin
from .models import Musician

@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'instrument_type', 'email')
    
