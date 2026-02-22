from django import forms
from .models import Talaba


class TalabaForm(forms.ModelForm):
    class Meta:
        model = Talaba
        fields = ['ism_familya', 'telefon', 'telegram']
        widgets = {
            'ism_familya': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': "Masalan: Abdullayev Jasur"
            }),
            'telefon': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': '+998 90 123 45 67'
            }),
            'telegram': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': '@username (ixtiyoriy)'
            }),
        }
        labels = {
            'ism_familya': "Ism-familya",
            'telefon':     "Telefon raqami",
            'telegram':    "Telegram username",
        }
