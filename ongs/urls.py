from django.urls import path

from .views import OngsView, OngAddView, OngUpdateView, OngDeleteView

urlpatterns = [
    path('ongs', OngsView.as_view(), name='ongs'),
    path('ong/adicionar/', OngAddView.as_view(), name='ong_adicionar'),
    path('<int:pk>/ong/editar/', OngUpdateView.as_view(), name='ong_editar'),
    path('<int:pk>/ong/apagar/', OngDeleteView.as_view(), name='ong_apagar'),
]