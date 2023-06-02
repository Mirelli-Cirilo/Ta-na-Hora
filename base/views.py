from django.shortcuts import render, redirect
from .models import Remedio
from .forms import Remedioforms
from django.http import HttpResponse

def home(request):
    medicamentos = Remedio.objects.all()
    form = Remedioforms

    if request.method == 'POST':
        form = Remedioforms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return HttpResponse('Dados inválidos')

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




