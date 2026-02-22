from django import forms
from .models import Group


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'total_tasks', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Masalan: Python 101-guruh'}),
            'total_tasks': forms.NumberInput(attrs={'class': 'form-input', 'min': 1, 'max': 200}),
            'description': forms.Textarea(attrs={'class': 'form-input', 'rows': 3, 'placeholder': 'Guruh haqida qisqacha...'}),
        }
        labels = {
            'name': 'Guruh nomi',
            'total_tasks': 'Jami vazifalar soni',
            'description': 'Tavsif (ixtiyoriy)',
        }
