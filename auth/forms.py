from django import forms


class RegUser(forms.Form):
    username = forms.CharField(label='Имя:', max_length=100)
    password = forms.CharField(label='Пароль:', max_length=25, widget=forms.PasswordInput())
    password_check = forms.CharField(label='Еще раз:', max_length=25, widget=forms.PasswordInput())