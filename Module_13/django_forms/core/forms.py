from django import forms 

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
