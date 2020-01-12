from django import forms
from django.core.exceptions import ValidationError

from members.models import User


class SignupForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'email'
            }
        )
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={

            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={

            }
        )
    )
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={

            }
        )
    )

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise ValidationError('이미 사용중인 이메일입니다')

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise ValidationError('이미 사용중인 username입니다.')

    def signup(self):
        email = self.cleaned_data['email']
        username = self.cleaned_data['username']
        name = self.cleaned_data['name']
        password = self.cleaned_data['password']

        return User.objects.create(email=email, name=name, username=username, password=password)
