from django import forms
from .models import Author
import re

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        
        widgets = {
            'bio' : forms.Textarea(attrs={'rows':4})
        }
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not re.match(r'^[a-zA-Z\s]+$', name):
            raise forms.ValidationError("Name must contain only letters and spaces")
        return name
    
    def clean_phone(self):
        if self.cleaned_data.get('phone'):
            phone = self.cleaned_data.get('phone')
            if phone.isalpha():
                raise forms.ValidationError("Phone number must be a numric digit")
            return phone
        else:
            pass