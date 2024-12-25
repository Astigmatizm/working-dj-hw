from django import forms
from .models import Record, IceCream, Document
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox


class LoginUserForm(forms.Form):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['title', 'content']


class IceCreamForm(forms.ModelForm):
    class Meta:
        model = IceCream
        fields = ['name', 'flavor', 'price', 'is_available']


class CustomForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'file']