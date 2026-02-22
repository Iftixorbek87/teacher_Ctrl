from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ism va familiya'}),
        }
        labels = {
            'full_name': "O'quvchining to'liq ismi",
        }
