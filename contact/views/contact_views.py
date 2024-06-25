from django.shortcuts import render, get_object_or_404
from contact.models import Contato
from django.http import Http404
# Create your views here.

def index(request):
    contact = Contato.objects.all()\
    .filter(show=True)\
    .order_by('-id')[10:20]
    
    context = { 
        'contact':contact,
        'site_title': 'Contatos - '
    }
    return render(
        request,
        'contact/index.html',
        context
    )

def contact(request, contact_id):
    # single_contact = Contato.objects.filter(id=contact_id).first()
    single_contact = get_object_or_404(
        Contato, pk=contact_id,show=True)

    contact_name = f'{single_contact.first_name}  {single_contact.last_name} - '
    context = { 
        'contact':single_contact,
        'site_title': contact_name
    }
    return render(
        request,
        'contact/contact.html',
        context
    )