from django import forms
from .models import Profile
import re

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        
        widgets = {
            'about' : forms.Textarea(attrs={'rows':4})
        }
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not re.match(r'^[a-zA-Z\s]+$', name):
            raise forms.ValidationError("Name must contain only letters and spaces")
        return name
   