from django.core.exceptions import ValidationError
from django import forms
from contact.models import Contato

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'classe-a classe-b',
                'placeholder':'Digite o seu nome',
                   }
        ),
        label='Primeiro Nome',
        help_text='Texto de ajuda pra seu usuário',
    )
    qualquer_coisa = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'classe-a classe-b',
                'placeholder':'Digite o seu nome',
                   }
        ),
        
        help_text='Texto de ajuda pra seu usuário',
    )

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    class Meta:
        model = Contato
        fields = (
            'first_name','last_name','phone'
            )
        
        
    def clean(self) -> None:
        cleaned_data = self.cleaned_data
        
        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de Erro',
                code='invalid',
            )
    
        )
        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de Erro2',
                code='invalid',
            )
        )

        return super().clean()