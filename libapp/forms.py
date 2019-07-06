from django import forms
from .models import bookdata,studentdata

class ContactForm(forms.ModelForm):
    class Meta:
        model = studentdata
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(),
        }

class userform(forms.ModelForm):
    class Meta:
        model = studentdata
        fields = ('Username','password')
        widgets = {
            'password': forms.PasswordInput(),
        }

class searchform(forms.ModelForm):
    class Meta:
        model = bookdata
        fields = ['Book_name']


