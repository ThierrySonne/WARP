from django.urls import path

from .views import AgentesView, AgenteAddView, AgenteUpdateView, AgenteDeleteView, AgenteInLineEditView

urlpatterns = [
    path('agentes', AgentesView.as_view(), name='agentes'),
    path('agente/adicionar/', AgenteAddView.as_view(), name='agente_adicionar'),
    path('<int:pk>/agente/editar/', AgenteUpdateView.as_view(), name='agente_editar'),
    path('<int:pk>/agente/apagar/', AgenteDeleteView.as_view(), name='agente_apagar'),
    path('<int:pk>/agente/inline/', AgenteInLineEditView.as_view(), name='agente_inline'),
]