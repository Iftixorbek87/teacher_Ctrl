from django import forms
from .models import Guruh


class GuruhForm(forms.ModelForm):
    class Meta:
        model = Guruh
        fields = ['nomi', 'jami_vazifalar', 'tavsif']
        widgets = {
            'nomi': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Masalan: A-guruh'}),
            'jami_vazifalar': forms.NumberInput(attrs={'class': 'form-input', 'min': 1, 'max': 300}),
            'tavsif': forms.Textarea(attrs={'class': 'form-input', 'rows': 3, 'placeholder': 'Ixtiyoriy...'}),
        }
        labels = {
            'nomi': 'Guruh nomi',
            'jami_vazifalar': 'Jami vazifalar soni',
            'tavsif': 'Tavsif',
        }
