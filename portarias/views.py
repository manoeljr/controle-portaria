from django.shortcuts import render, redirect
from portarias.forms import VisitForm
from portarias.models import Visitantes

def index(request):
    visitante = Visitantes.objects.all()
    data={}
    data['lista_visitants'] = visitante
    return render(request, 'portarias/index.html', data)


def adicionarVisitante(request):
    form = VisitForm(request.POST or None)
    context = {'form':form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            redirect(request, 'portarias/horarios.html')

    return render(request, 'portarias/adicionar-visitante.html', context)

def adicionarHorarios(request, pk):
    return render(request, 'portarias/horarios.html')