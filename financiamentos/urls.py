from django.urls import path

from .views import FinanciamentosView, FinanciamentoAddView, FinanciamentoUpdateView, FinanciamentoDeleteView

urlpatterns = [
    path('financiamentos', FinanciamentosView.as_view(), name='financiamentos'),
    path('financiamento/adicionar', FinanciamentoAddView.as_view(), name='financiamento_adicionar'),
    path('<int:pk>/financiamento/editar/', FinanciamentoUpdateView.as_view(), name='financiamento_editar'),
    path('<int:pk>/financiamento/apagar/', FinanciamentoDeleteView.as_view(), name='financiamento_apagar'),

]