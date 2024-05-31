from django import forms
from django.forms.widgets import NumberInput, DateInput
import datetime
from django.core import validators

class Form_1(forms.Form):
    name = forms.CharField(max_length=50, 
                           initial='Shahid Afridi',
                           help_text = "Enter your name between 50 charecters")
    about = forms.CharField(
                        max_length=200,
                        required=False, 
                        widget = forms.Textarea(attrs={'rows':4}),
                        )
    email = forms.EmailField(label="Please Enter Your Email")
    married = forms.BooleanField(required=False, initial=True)
    dob = forms.DateField(widget=NumberInput(attrs={'type':'date'}))
    # # dob = forms.DateField(widget=DateInput(attrs={'type':'date'})) #same as above
    BIRTH_YEAR_CHOICES = [1997,1998,1999]
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years= BIRTH_YEAR_CHOICES)) #here year will show the choices value
    # birth_year = forms.DateField(widget=forms.SelectDateWidget) # here all year will be shown
    
    submission_date = forms.DateField(
        widget=forms.DateInput(attrs = {'type':'date'}),
        initial= datetime.date.today
    )
    
    weight = forms.DecimalField()
        
        
    FAVORITE_COLORS_CHOICES = [
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
    ]

    favorite_color = forms.ChoiceField(
        choices=FAVORITE_COLORS_CHOICES,
        widget=forms.RadioSelect
        )
    # favorite_colors = forms.MultipleChoiceField(
    #     choices=FAVORITE_COLORS_CHOICES,
    #     widget=forms.CheckboxSelectMultiple)
    
    
class Form_2(forms.Form):
    name = forms.CharField(max_length=50, 
                           initial='Shahid Afridi',
                           label = "Your Name",
                           label_suffix= 'hello',
                           help_text = "Enter your name between 50 charecters")
    file = forms.FileField(
        help_text = "Please provide PDF or Docx file",
        validators=[validators.FileExtensionValidator(allowed_extensions=['pdf', 'docx'], message='.pdf and .docx only')]  #built-in validators
    )
    profile_image = forms.ImageField(
        help_text = "Please provide png image",
        validators=[validators.FileExtensionValidator(allowed_extensions=['png'], message='png image allowed only')]  #built-in validators
    )
    # profile_image = forms.ImageField()
    
    portfolio_link = forms.URLField()
    
    
    
    # def clean_file(self): #manual validators
    #     file = self.cleaned_data.get('file')
    #     if file:
    #         if not file.name.endswith(('.pdf', '.png')):
    #             raise forms.ValidationError('File must be .pdf or .png')
    #     return file
   
        