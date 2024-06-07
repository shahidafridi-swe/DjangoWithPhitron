from django import forms

from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content','image', 'category')
        
        widgets = {
            'category' : forms.CheckboxSelectMultiple
        }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        labels = {
            'body': 'Comment'
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email'}),
            'body': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Your Comment'})
        }