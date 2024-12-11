from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import AgenteModelForm
from .models import Agente


class AgentesView(ListView):
    model = Agente
    template_name = 'agentes.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(AgentesView, self).get_queryset()
        if buscar:
            return qs.filter(nome__icontains=buscar)

        if qs.count() > 0:
            paginator = Paginator(qs, 100)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, 'Não existem Agentes cadastrados!')

class AgenteAddView(SuccessMessageMixin, CreateView):
    model = Agente
    form_class = AgenteModelForm
    template_name = 'Agente_form.html'
    success_url = reverse_lazy('agentes')
    success_message = 'Agente cadastrado com sucesso!'

class AgenteUpdateView(SuccessMessageMixin, UpdateView):
    model = Agente
    form_class = AgenteModelForm
    template_name = 'Agente_form.html'
    success_url = reverse_lazy('agentes')
    success_message = 'Agente atualizado com sucesso!'

class AgenteDeleteView(SuccessMessageMixin, DeleteView):
    model = Agente
    template_name = 'Agente_apagar.html'
    success_url = reverse_lazy('agentes')
    success_message = 'Agente apagado com sucesso!'