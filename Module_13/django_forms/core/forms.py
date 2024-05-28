from django import forms 
from django.core import validators
from django.core.validators import MinLengthValidator
import re

class ContactForm(forms.Form):
    name = forms.CharField(label='Username',widget=forms.TextInput({ "placeholder": "Your Name", "class": "form-control"}))
    email = forms.EmailField(label='Your Email',widget=forms.TextInput({ "placeholder": "Your Email", "class": "form-control"}))
    file = forms.FileField(required=False)
    
    about = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'placeholder': "Write about yourself..." , 'class': 'myClass'}))

    age = forms.IntegerField(initial=27, disabled=True)
    # age = forms.CharField(widget=forms.NumberInput())
    weight = forms.FloatField()
    balance = forms.DecimalField()
    married = forms.BooleanField(required=False)

    # birthday = forms.DateField(widget = forms.SelectDateWidget)
    # birthday = forms.DateField(widget = forms.DateInput(attrs={'type':'date'}))
    birthday = forms.CharField(widget = forms.DateInput(attrs={'type':'date'}))

    appoinment = forms.DateTimeField(widget = forms.DateInput(attrs={'type':'datetime-local'}))
    CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    ]
    size = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    MEAL = [('B', 'Biriyani'), ('C', 'Coffee'), ('T', 'Tea')]
    favouriteFood = forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple)



# class ValidationForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)
#     confirm_password = forms.CharField(widget=forms.PasswordInput)

#     def clean_name(self):
#         name = self.cleaned_data['name']
#         if len(name) < 3:
#             raise forms.ValidationError("Enter a name with at least 3 characters")
#         return name

#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         if not email.endswith('@gmail.com'):
#             raise forms.ValidationError("Email must be from the domain @gmail.com")
#         return email
    
#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get('password')
#         confirm_password = cleaned_data.get('confirm_password')
#         if len(password) < 6 or len(confirm_password) < 6:
#             raise forms.ValidationError("Password must be greater than or equal 6 digits")
#         if password and confirm_password and password != confirm_password:
#             raise forms.ValidationError("Passwords do not match")
        
#         return cleaned_data
    
class ValidationForm(forms.Form):
    name = forms.CharField(max_length=100,validators=[MinLengthValidator(3,'Enter a name with at least 3 characters')])
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput, validators=[MinLengthValidator(6,'Password must be greater than or equal 6 digits')])
    confirm_password = forms.CharField(widget=forms.PasswordInput, validators=[MinLengthValidator(6,'Password must be greater than or equal 6 digits')])
    
    # def clean_name(self):
    #     name = self.cleaned_data.get('name')
    #     if not name.isalpha():
    #         raise forms.ValidationError("Name must contain only letters")
    #     return name
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not re.match(r'^[a-zA-Z\s]+$', name):
            raise forms.ValidationError("Name must contain only letters and spaces")
        return name
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError("Email must be from the domain @gmail.com")
        return email
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data
    
    