from django.shortcuts import render
from contact.models import Contato

# Create your views here.

def index(request):
    contact = Contato.objects.all()

    context = { 
        'contact':contact
    }
    return render(
        request,
        'contact/index.html',
        context
    )