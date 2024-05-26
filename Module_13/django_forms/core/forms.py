from django import forms 

class ContactForm(forms.Form):
    name = forms.CharField(label='Username',widget=forms.TextInput({ "placeholder": "Your Name", "class": "form-control"}))
    email = forms.EmailField(label='Your Email',widget=forms.TextInput({ "placeholder": "Your Email", "class": "form-control"}))
    file = forms.FileField()
    
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    # married = forms.BooleanField(required=False)
    # birthday = forms.DateField(widget = forms.SelectDateWidget)
    # appoinment = forms.DateTimeField()
    # CHOICES = [
    #     ('S', 'Small'),
    #     ('M', 'Medium'),
    #     ('L', 'Large'),
    # ]
    # size = forms.ChoiceField(choices=CHOICES)
    # MEAL = [('B', 'Biriyani'), ('C', 'Coffee'), ('T', 'Tea')]
    # favouriteFood = forms.MultipleChoiceField(choices=MEAL)
