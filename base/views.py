from django.shortcuts import render, redirect
from .models import Remedio
from .forms import Remedioforms
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core.mail import send_mail
import sched
import time
from datetime import datetime, timedelta


def home(request):
    medicamentos = Remedio.objects.all()
    form = Remedioforms

    if request.method == 'POST':
        form = Remedioforms(request.POST)
        if not form.is_valid():   
            return HttpResponse('Dados inválidos')
        else:
            form.save()
            return redirect('/')
    
     
    context = {'medicamentos':medicamentos, 'form':form}

    return render(request, 'home.html', context)

def delete(request, id):
    medicamento = Remedio.objects.get(id=id)

    if request.method == 'POST':
        medicamento.delete()
        return redirect('/')
    
    context = {'medicamento': medicamento}
    return render(request, 'delete.html', context)

def update(request, id):
    medicamento = Remedio.objects.get(id=id)
    form = Remedioforms(instance=medicamento)

    if request.method == 'POST':
        form = Remedioforms(request.POST, instance=medicamento)

        if form.is_valid():
            form.save()
            return redirect('/')
        
      
    context = {'form':form}    
    return render(request, 'update.html', context)

def detail(request, id):
    medicamento = Remedio.objects.get(id=id)

    context = {'medicamento': medicamento}
    return render(request, 'details.html', context)

def envio_email(request, id):
    remedio = Remedio.objects.get(id=id)
    hora = str(remedio.horario)[0:2]
    min = str(remedio.horario)[3:5]
    email_user = request.user.email
    scheduler = sched.scheduler(time.time, time.sleep)
    
    def email():
        send_mail('Hora de Tomar seu remédio', f'Chegou a hora de tomar seu remédio {remedio.nome}', 'TanaHora1661@gmail.com', [email_user])
        scheduler.enterabs((datetime.now() + timedelta(seconds=50)).timestamp(), 1, email)
                
    def sche():
        scheduler.enterabs(datetime(year=2023, month=6, day=8, hour=int(hora), minute=int(min)).timestamp(), 1, email)
        
    sche()

    scheduler.run()
    return HttpResponse('passou')
