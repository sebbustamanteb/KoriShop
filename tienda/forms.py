from django import forms
from .models import form_consultas

class form_consultasForm(forms.ModelForm):
    class Meta:
        model = form_consultas
        fields = ['email', 'message']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su correo electrónico'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su mensaje',
                'rows': 4
            }),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError("El correo debe ser del dominio '@gmail.com'.")
        return email