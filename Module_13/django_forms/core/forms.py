from django import forms 
from django.core import validators

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
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)
#     def clean_name(self):
#         valName = self.cleaned_data['name']
#         if len(valName) < 10 :
#             raise forms.ValidationError("Enter a name with at least 10 characters")

class ValidationForm(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(10, message="Enter a name with at least 10 characters")])
    email = forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator(message="Enter a valid email")])
    age = forms.IntegerField(validators=[validators.MaxValueValidator(50,  message="age should be 18 to 50"), validators.MinValueValidator(18, message="age should be 18 to 50")])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'], message="File must be a pdf")])