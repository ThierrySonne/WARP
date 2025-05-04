from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import FinanciamentoModelForm
from .models import Financiamento

class FinanciamentosView(PermissionRequiredMixin, ListView):
    permission_required = 'financiamentos.view_financiamento'
    permission_denied_message = 'Vizualizar Financiamentos'
    model = Financiamento
    template_name = 'financiamentos.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(FinanciamentosView, self).get_queryset()
        if buscar:
            return qs.filter(nome__icontains=buscar)

        if qs.count() > 0:
            paginator = Paginator(qs, 100)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request,'Não existem Financiamentos')


class FinanciamentoAddView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = 'financiamentos.add_financiamento'
    permission_denied_message = 'Adicionar Financiamentos'
    model = Financiamento
    form_class = FinanciamentoModelForm
    template_name = 'financiamento_form.html'
    success_url = reverse_lazy('financiamentos')
    success_message = 'Financiamento Registado com Sucesso!'

class FinanciamentoUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = 'financiamentos.change_financiamento'
    permission_denied_message = 'Editar Financiamentos'
    model = Financiamento
    form_class = FinanciamentoModelForm
    template_name = 'financiamento_form.html'
    success_url = reverse_lazy('financiamentos')
    success_message = 'Financiamento Registado com Sucesso!'

class FinanciamentoDeleteView(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    permission_required = 'financiamentos.delete_financiamento'
    permission_denied_message = 'Deletar Financiamentos'
    model = Financiamento
    template_name = 'financiamento_apagar.html'
    success_url = reverse_lazy('financiamentos')
    success_message = 'Financiamento Apagado com Sucesso!'