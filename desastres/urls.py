from django.urls import path

from .views import DesastresView, DesastreAddView, DesastreUpdateView, DesastreDeleteView

urlpatterns = [
    path('desastres', DesastresView.as_view(), name='desastres'),
    path('desastre/adicionar',DesastreAddView.as_view(), name='desastre_adicionar'),
    path('<int:pk>/desastre/editar',DesastreUpdateView.as_view(), name='desastre_editar'),
    path('<int:pk>/desastre/apagar',DesastreDeleteView.as_view(), name='desastre_apagar'),
]