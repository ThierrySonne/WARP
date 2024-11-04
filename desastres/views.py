from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import DesastreModelForm
from .models import Desastre

class DesastresView(ListView):
    model = Desastre
    template_name = 'desastres.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(DesastresView, self).get_queryset()
        if buscar:
            return qs.filter(nome__icontains=buscar)

        if qs.count() > 0:
            paginator = Paginator(qs, 10)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request,'Não existem Desastres Reportados Atualmente')


class DesastreAddView(SuccessMessageMixin, CreateView):
    model = Desastre
    form_class = DesastreModelForm
    template_name = 'desastre_form.html'
    success_url = reverse_lazy('Desastres')
    success_message = 'Desastre Registado com Sucesso!'