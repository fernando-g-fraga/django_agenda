from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from contact.forms import RegisterForm

def register(request):
    form = RegisterForm

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Usuário Registrado')
            return redirect('contact:login')


    return render(
        request,
        'contact/register.html',
        {
            'form':form
        },
    )

def loginview(request):
    form = AuthenticationForm(request)


    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)


        if form.is_valid():
            user = form.get_user()
            auth.login(request,user)
            messages.success(request,'Logado com sucesso')
            return redirect('contact:index')
        messages.error(request,'Login inválido')

    return render(
        request,
        'contact/login.html',
        {
            'form':form
        },
    )

def logoutview(request):
    auth.logout(request)
    return redirect('contact:login')
