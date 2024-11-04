from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import AbrigoModelForm
from .models import Abrigo

class AbrigosView(ListView):
    model = Abrigo
    template_name = 'abrigos.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(AbrigosView, self).get_queryset()
        if buscar:
            return qs.filter(nome__icontains=buscar)

        if qs.count() > 0:
            paginator = Paginator(qs, 10)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request,'Não existem Abrigos')


class AbrigoAddView(SuccessMessageMixin, CreateView):
    model = Abrigo
    form_class = AbrigoModelForm
    template_name = 'abrigo_form.html'
    success_url = reverse_lazy('Abrigos')
    success_message = 'Abrigo Adicionado com Sucesso!'