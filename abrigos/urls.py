from django.urls import  path

from .views import AbrigosView, AbrigoAddView

urlpatterns = [
    path('abrigos', AbrigosView.as_view(), name='abrigos'),
    path('abrigos/adicionar', AbrigoAddView.as_view(), name='abrigo_adicionar'),
]