from django.urls import path

from .views import OngsView

urlpatterns = [
    path('ongs', OngsView.as_view(), name='ongs'),
]