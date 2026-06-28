from django import forms
from .models import Tweet,Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:
        model=Tweet
        fields=['text','photo']

class UserRegistarionForm(UserCreationForm):
    email=forms.EmailField()
    class Meta: 
        model=User
        fields=('username','email','password1','password2')

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
 