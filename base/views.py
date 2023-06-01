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


