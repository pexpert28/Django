from django import forms
from Shelegram.models import ShelegramUser, ShelegramGroup


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = ShelegramUser
        fields = ('first_name', 'last_name','email', 'username', 'password', 'picture')


class EditForm(forms.ModelForm):

    class Meta:
        model = ShelegramUser
        fields = ('first_name', 'last_name', 'email', 'picture')


class GroupCreationForm(forms.ModelForm):

    class Meta:
        model = ShelegramGroup
        fields = ('name', 'picture');
