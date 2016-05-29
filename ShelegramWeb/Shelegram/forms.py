from django import forms
from Shelegram.models import ShelegramUser


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = ShelegramUser
        fields = ('first_name', 'last_name','email', 'username', 'password', 'picture')