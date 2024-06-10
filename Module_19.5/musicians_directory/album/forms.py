from django.forms import ModelForm
from django import forms

from .models import Album

class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

        labels = {
            "name" : "Album Name"
        }