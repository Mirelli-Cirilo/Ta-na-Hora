from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages import constants

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if senha != confirmar_senha:
            return HttpResponse('Digite a senha igualmente nos dois campos')
        
        user = User.objects.filter(username=username)

        if user:
            return HttpResponse('Este nomde de usuário já está sendo utilizado.')

        user = User.objects.create_user(username=username, email=email, password=senha)
        login(request, user)

        return redirect(reverse('home'))

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'GET':
        return render(request, 'login.html')

    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        try:
            user = User.objects.get(username=username)
        except:
            messages.add_message(request, constants.ERROR, 'Usuário não foi encontrado.')
        
        user = authenticate(username=username, password=senha)

        if user:
            login(request, user)
            return redirect(reverse('home'))
        else:
            messages.add_message(request, constants.ERROR, 'Nome de usuário ou senha incorretos')
        
def logoutPage(request):
    logout(request)    

    return redirect(reverse('home'))    
