from django.shortcuts import render, redirect
from .models import Remedio
from .forms import Remedioforms
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



def envio_email(request):
    
    scheduler = sched.scheduler(time.time, time.sleep)

    def email():
        send_mail('Hora de Tomar seu remédio', 'Chegou a hora de tomar seu remédio', 'mirellicirilo44@gmail.com', ['mariamirellicirilo@gmail.com'])
        scheduler.enterabs((datetime.now() + timedelta(seconds=10)).timestamp(), 1, email)
                
    def sche():
        scheduler.enterabs(datetime(year=2023, month=6, day=6, hour=15, minute=11).timestamp(), 1, email)
        
    sche()

    scheduler.run()
    return HttpResponse('passou')
