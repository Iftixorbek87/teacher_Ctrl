from django import forms
from .models import Patok


class PatokForm(forms.ModelForm):
    class Meta:
        model = Patok
        fields = ['nomi', 'tavsif']
        widgets = {
            'nomi': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Masalan: 2024-yil 1-patok'}),
            'tavsif': forms.Textarea(attrs={'class': 'form-input', 'rows': 3, 'placeholder': 'Ixtiyoriy...'}),
        }
        labels = {'nomi': 'Patok nomi', 'tavsif': 'Tavsif'}
