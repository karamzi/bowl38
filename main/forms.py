from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class LoginUserForm(AuthenticationForm, forms.ModelForm):
    username = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Введите Логин'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise ValidationError(
                'Дождитесь активации администратором!',
                code='no_active'
            )

    class Meta:
        model = User
        fields = ('username', 'password')


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Введите логин'}))
    first_name = forms.CharField(required=True, max_length=30,
                                 widget=forms.TextInput(attrs={'placeholder': 'Введите имя'}))
    last_name = forms.CharField(required=True, max_length=30,
                                widget=forms.TextInput(attrs={'placeholder': 'Введите фамилию'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'}))

    def clean(self):
        super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            errors = {'password2': 'Пароли не совпадают'}
            raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = False
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')
