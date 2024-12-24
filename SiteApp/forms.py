from django import forms
from .models import UserData


class LoginUserForm(forms.Form):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class MyForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)


class UserDataForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['name', 'email']

    def clean_name(self):    # Дополнительная валидация, если необходимо
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError("Имя должно быть длиннее 2 символов.")
        return name

    def clean_email(self):
        email = self.cleaned_data['email']
        if UserData.objects.filter(email=email).exists():        # Проверка уникальности email
            raise forms.ValidationError("Этот email уже существует в базе данных.")
        return email