from django.urls import path
from . import views

urlpatterns = [
    # Especialidade
    path('especialidades/', views.especialidade_list, name='especialidade_list'),
    path('especialidades/novo/', views.especialidade_create, name='especialidade_create'),
    path('especialidades/<int:pk>/editar/', views.especialidade_update, name='especialidade_update'),
    path('especialidades/<int:pk>/deletar/', views.especialidade_delete, name='especialidade_delete'),

    # Médico
    path('medicos/', views.medico_list, name='medico_list'),
    path('medicos/novo/', views.medico_create, name='medico_create'),
    path('medicos/<int:pk>/editar/', views.medico_update, name='medico_update'),
    path('medicos/<int:pk>/deletar/', views.medico_delete, name='medico_delete'),
]
