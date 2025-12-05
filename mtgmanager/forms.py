from django import forms
from django.contrib.auth.models import User

class ImportarCartasForm(forms.Form):
    nomes = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 10, 'cols': 50}),
        help_text="Cole os nomes das cartas, um por linha."
    )

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']