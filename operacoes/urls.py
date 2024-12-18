from django.urls import path


from .views import OperacoesView, OperacoesAddView, OperacoesUpdateView, OperacoesDeleteView

urlpatterns = [
    path('operacoes', OperacoesView.as_view(), name='operacoes'),
    path('adicionar/', OperacoesAddView.as_view(), name='operacoes_adicionar'),
    path('<int:pk>/operacoes/editar', OperacoesUpdateView.as_view(), name='operacoes_editar'),
    path('<int:pk>/operacoes/apagar', OperacoesDeleteView.as_view(), name='operacoes_apagar'),
]