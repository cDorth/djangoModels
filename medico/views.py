from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Especialidade, Medico
from .forms import EspecialidadeForm, MedicoForm

# ---------- ESPECIALIDADE GENERIC VIEWS ----------
class EspecialidadeListView(ListView):
    model = Especialidade
    template_name = 'medico/especialidade_list.html'
    context_object_name = 'especialidades'

class EspecialidadeCreateView(CreateView):
    model = Especialidade
    form_class = EspecialidadeForm
    template_name = 'medico/especialidade_form.html'
    success_url = reverse_lazy('especialidade_list')

class EspecialidadeUpdateView(UpdateView):
    model = Especialidade
    form_class = EspecialidadeForm
    template_name = 'medico/especialidade_form.html'
    success_url = reverse_lazy('especialidade_list')

class EspecialidadeDeleteView(DeleteView):
    model = Especialidade
    template_name = 'medico/confirm_delete.html'
    success_url = reverse_lazy('especialidade_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tipo'] = 'Especialidade'
        return context

# ---------- MÉDICO GENERIC VIEWS ----------
class MedicoListView(ListView):
    model = Medico
    template_name = 'medico/medico_list.html'
    context_object_name = 'medicos'

class MedicoCreateView(CreateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'medico/medico_form.html'
    success_url = reverse_lazy('medico_list')

class MedicoUpdateView(UpdateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'medico/medico_form.html'
    success_url = reverse_lazy('medico_list')

class MedicoDeleteView(DeleteView):
    model = Medico
    template_name = 'medico/confirm_delete.html'
    success_url = reverse_lazy('medico_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tipo'] = 'Médico'
        return context
