from django import forms

class LoginForms(forms.Form):
    username = forms.CharField(
        label='Usuário',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Seu nome de usuário'
            }
        ) 
    )

    password = forms.CharField(
        label='Senha',
        required=True,
        max_length=20,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Sua senha'
            }
        )
    )