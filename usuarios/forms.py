from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label='Nome de login',
        required=True,  
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Ex.: Hiago Lima'
            }
        ),
    )
    senha = forms.CharField( 
        label='Senha', required=True,  
        max_length=100,  
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Digite sua Senha'
            }
        ),
    )

class CadastroForms(forms.Form):
    nome_completo = forms.CharField(
        label='Nome de login',
        required=True,  
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Ex.: Hiago Lima'
            }
        ),
    )
    email = forms.EmailField(
        label='Nome de login',
        required=True,  
        max_length=100,
        widget=forms.EmailInput(
             attrs={
                'class':'form-control',
                'placeholder': 'Ex.: hiagolima@email.com'
            }
        )
    )
    senha = forms.CharField(
        label='Nome de login',
        required=True,  
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Ex.: Hiago Lima'
            }
        ),
    )
    confirmacao_senha = forms.CharField(
        label='Nome de login',
        required=True,  
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Ex.: Hiago Lima'
            }
        ),
    )
