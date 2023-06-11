from django.shortcuts import render, redirect
from .models import Remedio
from .forms import Remedioforms
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.mail import send_mail
import sched
import time
from datetime import datetime, timedelta

@login_required(login_url='login')
def home(request):
    medicamentos = Remedio.objects.filter(user=request.user.id)[0:7]
    form = Remedioforms

    if request.method == 'POST':
        form = Remedioforms(request.POST)
        if not form.is_valid():   
            return HttpResponse('Dados inválidos')
        else:
            user = form.save(commit=False)
            user.user = request.user
            user.save()
            return render(request, 'email_template.html', {'medicamento': user})
    
     
    context = {'medicamentos':medicamentos, 'form':form}

    return render(request, 'home.html', context)

@login_required(login_url='login') 
def delete(request, id):
    medicamento = Remedio.objects.get(id=id)

    if request.method == 'POST':
        medicamento.delete()
        return redirect('/')
    
    context = {'medicamento': medicamento}
    return render(request, 'delete.html', context)

@login_required(login_url='login') 
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

@login_required(login_url='login') 
def detail(request, id):
    medicamento = Remedio.objects.get(id=id)

    context = {'medicamento': medicamento}
    return render(request, 'details.html', context)

@login_required(login_url='login') 
def envio_email(request, id):
    
    remedio = Remedio.objects.get(id=id)
    hora = str(remedio.horario)[0:2]
    min = str(remedio.horario)[3:5]
    hora = int(hora)
    min = int(min)
    email_user = request.user.email
    scheduler = sched.scheduler(time.time, time.sleep)
    
    def email():
        send_mail('Hora de Tomar seu remédio', f'Chegou a hora de tomar seu remédio {remedio.nome}', 'TanaHora1661@gmail.com', [email_user])
        scheduler.enterabs((datetime.now() + timedelta(hours=8)).timestamp(), 1, email)
       
    def sche():
        scheduler.enterabs(datetime(year=2023, month=6, day=10, hour=hora, minute=min).timestamp(), 1, email)
        
    sche()

    scheduler.run()
    return HttpResponse('passou')
