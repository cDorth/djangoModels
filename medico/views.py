from django.shortcuts import render, redirect, get_object_or_404
from .models import Especialidade, Medico
from .forms import EspecialidadeForm, MedicoForm

# ---------- ESPECIALIDADE ----------
def especialidade_list(request):
    especialidades = Especialidade.objects.all()
    return render(request, 'medico/especialidade_list.html', {'especialidades': especialidades})

def especialidade_create(request):
    if request.method == "POST":
        form = EspecialidadeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('especialidade_list')
    else:
        form = EspecialidadeForm()
    return render(request, 'medico/especialidade_form.html', {'form': form})

def especialidade_update(request, pk):
    especialidade = get_object_or_404(Especialidade, pk=pk)
    if request.method == "POST":
        form = EspecialidadeForm(request.POST, instance=especialidade)
        if form.is_valid():
            form.save()
            return redirect('especialidade_list')
    else:
        form = EspecialidadeForm(instance=especialidade)
    return render(request, 'medico/especialidade_form.html', {'form': form})

def especialidade_delete(request, pk):
    especialidade = get_object_or_404(Especialidade, pk=pk)
    if request.method == "POST":
        especialidade.delete()
        return redirect('especialidade_list')
    return render(request, 'medico/confirm_delete.html', {'object': especialidade, 'tipo': 'Especialidade'})

# ---------- MÉDICO ----------
def medico_list(request):
    medicos = Medico.objects.all()
    return render(request, 'medico/medico_list.html', {'medicos': medicos})

def medico_create(request):
    if request.method == "POST":
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medico_list')
    else:
        form = MedicoForm()
    return render(request, 'medico/medico_form.html', {'form': form})

def medico_update(request, pk):
    medico = get_object_or_404(Medico, pk=pk)
    if request.method == "POST":
        form = MedicoForm(request.POST, instance=medico)
        if form.is_valid():
            form.save()
            return redirect('medico_list')
    else:
        form = MedicoForm(instance=medico)
    return render(request, 'medico/medico_form.html', {'form': form})

def medico_delete(request, pk):
    medico = get_object_or_404(Medico, pk=pk)
    if request.method == "POST":
        medico.delete()
        return redirect('medico_list')
    return render(request, 'medico/confirm_delete.html', {'object': medico, 'tipo': 'Médico'})
