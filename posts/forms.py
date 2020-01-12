from django import forms

from posts.models import Post


class PostCreateForm(forms.Form):
    images = forms.ImageField(
        widget=forms.ClearableFileInput(
            attrs={
                'multiple': True
            }
        )
    )
    content = forms.CharField(
        widget=forms.TextInput()
    )
