from django import forms
from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=('full_name','email','phone','message')
        widgets={
           
            'full_name': forms.TextInput(attrs={
            'class':'w-100 py-2 px-3 mb-3',
            }),
            'email': forms.EmailInput(attrs={
            'class':'w-100 py-2 px-3 mb-3',
            }),
            'phone': forms.TextInput(attrs={
            'class':'w-100 py-2 px-3 mb-3',
            }),
            'message': forms.Textarea(attrs={
            'class':'w-100 py-2 px-3 mb-3',
            'rows':5,

            })
        }


class HomeContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=('full_name','email','phone','message')
        widgets={
           
            'full_name': forms.TextInput(attrs={
            'class':'w-100 mt-4',
            'placeholder':'Adınız və Soyadınız'
            }),
            'email': forms.EmailInput(attrs={
            'class':'w-100 mt-4',
            'placeholder':'Elektron poçt ünvanınız'
            }),
            'phone': forms.TextInput(attrs={
            'class':'w-100 mt-4',
            'placeholder':'Telefon nömrəniz'
            }),
            'message': forms.Textarea(attrs={
            'class':'w-100 mt-4',
            'placeholder':'Mesajınız',
            'rows':5,

            })
        }

