from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models
class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept':'image/*'
            }
        )
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Aqui veio do init',
            }
        ),
        label='Primeiro Nome',
        help_text='Texto de ajuda para seu usuário',
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['first_name'].widget.attrs.update({
        #     'class': 'classe-a classe-b',
        #     'placeholder': 'Aqui veio do init',
        # })
    class Meta:
        model = models.Contato
        fields = (
            'first_name', 'last_name', 'phone','email','description','Categoria','picture',    
        )
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class': 'classe-a classe-b',
        #             'placeholder': 'Escreva aqui',
        #         }
        #     )
        # }

    def clean(self):
        cleaned_data = self.cleaned_data

        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError('Os dois campos nao podem coincidir.')
            self.add_error('first_name',msg)
            self.add_error('last_name',msg)


        return super().clean()
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name == 'ABC':
           self.add_error(
            'first_name',
            ValidationError(
                'add error',
                code='invalid'
            )
        )
        return first_name

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(min_length=3, max_length=11, required=True)
    last_name = forms.CharField(min_length=3, max_length=11, required=True)
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = (
                  'first_name',
                  'last_name',
                  'email',
                  'username',
                  'password1',
                  'password2',
                  )
        
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error('email',ValidationError('O Email informado já existe.', code='invalid')) 

        return email

