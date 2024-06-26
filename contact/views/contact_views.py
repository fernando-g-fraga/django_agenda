from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from contact.models import Contato
from django.http import Http404
# Create your views here.

def index(request):
    contact = Contato.objects.all()\
    .filter(show=True)\
    .order_by('-id')
    paginator = Paginator(contact,10)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    
    context = { 
        'page_obj':page_obj,
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
# Entry.objects.get(headline__contains="Lennon")

def search(request):
    search_value = request.GET.get('q','').strip()

    if len(search_value) == 0:
        return redirect('contact:index')

    print(search_value)

    contact = Contato.objects.all()\
    .filter(show=True)\
    .filter(
       Q(first_name__icontains=search_value) | \
        Q(last_name__icontains=search_value) |\
        Q(phone__icontains=search_value) |\
        Q(email__icontains=search_value))\
    
    print(contact.query)

    paginator = Paginator(contact,10)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = { 
        'page_obj':page_obj,
        'site_title': 'Search - ',
        'search_value': search_value
    }
    return render(
        request,
        'contact/index.html',
        context,


        
    )