from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    password = forms.CharField(
        label="",
        max_length=50,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )
