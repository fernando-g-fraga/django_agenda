from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.functional import SimpleLazyObject

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

class UpdateRegisterForm(forms.ModelForm):
    first_name = forms.CharField(
        label='Primeiro Nome',
        min_length=2, 
        max_length=30,
        required=True,
        help_text='Este campo é obrigatório',
        error_messages={
            'min_length':"Por favor, adicione mais de duas letras"
        }
    )

    last_name = forms.CharField(
        label='Primeiro Nome',
        min_length=2, 
        max_length=30,
        required=True,
        help_text='Este campo é obrigatório',
        error_messages={
            'min_length':"Por favor, adicione mais de duas letras"
        }
    )
    password1 = forms.CharField(
        label='Password 1',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_texts(),
        required=False,
    )
    password2 = forms.CharField(
        label='Password 2',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='Utilize a mesma senha informada anteriormente.',
        required=False,
    )


    class Meta:
        model = User
        fields = (
                  'first_name',
                  'last_name',
                  'email',
                  'username',                                                                                                                                          
                  )

    def save(self,commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)
        print(type(user))

        if isinstance(user, SimpleLazyObject):
            user = user._wrapped
               
        

        password = cleaned_data.get('password1')

        if password:
            user.set_password(password)

        if commit:
            user.save()

        return user



    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                self.add_error('password2',ValidationError('As senhas não batem'))

        return super().clean()
        
    def clean_email(self):
            email = self.cleaned_data.get('email')
            current_email = self.instance.email

            if current_email != email:
                    if User.objects.filter(email=email).exists():
                        self.add_error('email',ValidationError('O Email informado já existe.', code='invalid')) 

            return email
    
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1: 
            try:
               password_validation.validate_password(password1)
            except ValidationError as errors:
               self.add_error('password1',ValidationError(errors))        

        return password1



