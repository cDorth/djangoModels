from django.urls import path
from . import views

urlpatterns = [
    # Especialidade
    path('especialidades/', views.EspecialidadeListView.as_view(), name='especialidade_list'),
    path('especialidades/novo/', views.EspecialidadeCreateView.as_view(), name='especialidade_create'),
    path('especialidades/<int:pk>/editar/', views.EspecialidadeUpdateView.as_view(), name='especialidade_update'),
    path('especialidades/<int:pk>/deletar/', views.EspecialidadeDeleteView.as_view(), name='especialidade_delete'),

    # Médico
    path('medicos/', views.MedicoListView.as_view(), name='medico_list'),
    path('medicos/novo/', views.MedicoCreateView.as_view(), name='medico_create'),
    path('medicos/<int:pk>/editar/', views.MedicoUpdateView.as_view(), name='medico_update'),
    path('medicos/<int:pk>/deletar/', views.MedicoDeleteView.as_view(), name='medico_delete'),
]
