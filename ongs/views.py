from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import OngModelForm
from .models import Ong


class OngsView(ListView):
    model = Ong
    template_name = 'ongs.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(OngsView, self).get_queryset()
        if buscar:
            return qs.filter(nome__icontains=buscar)

        if qs.count() > 0:
            paginator = Paginator(qs, 1)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, 'Não existem ONGs cadastradas!')

class OngAddView(SuccessMessageMixin, CreateView):
    model = Ong
    form_class = OngModelForm
    template_name = 'Ong_form.html'
    success_url = reverse_lazy('Ongs')
    success_message = 'Ong cadastrada com sucesso!'

class OngUpdateView(SuccessMessageMixin, UpdateView):
    model = Ong
    form_class = OngModelForm
    template_name = 'Ong_form.html'
    success_url = reverse_lazy('Ongs')
    success_message = 'Ong atualizada com sucesso!'

class OngDeleteView(SuccessMessageMixin, DeleteView):
    model = Ong
    template_name = 'Ong_apagar.html'
    success_url = reverse_lazy('Ongs')
    success_message = 'Ong apagada com sucesso!'