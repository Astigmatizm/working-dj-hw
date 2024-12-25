from django import forms
from .models import Record, IceCream


class LoginUserForm(forms.Form):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['title', 'content']


class IceCreamForm(forms.ModelForm):
    class Meta:
        model = IceCream
        fields = ['name', 'flavor', 'price', 'is_available']