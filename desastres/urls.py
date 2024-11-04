from django.urls import path

from .views import DesastresView, DesastreAddView

urlpatterns = [
    path('desastres', DesastresView.as_view(), name='desastres'),
    path('desastre/adicionar',DesastreAddView.as_view(), name='desastre_adicionar'),
]