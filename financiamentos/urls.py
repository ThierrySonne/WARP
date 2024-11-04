from django.urls import path

from .views import FinanciamentosView, FinanciamentoAddView

urlpatterns = [
    path('financiamentos', FinanciamentosView.as_view(), name='financiamentos'),
    path('financiamento/adicionar', FinanciamentoAddView.as_view(), name='financiamento_adicionar'),

]