
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View, DetailView
from django.contrib import messages
from django.views.generic.base import TemplateResponseMixin

from operacoes.forms import OperacoesListForm, OperacoesModelForm
from operacoes.models import Operacoes


class OperacoesView( ListView):
    permission_denied_message = 'Vizualizar Operacoes'
    model = Operacoes
    template_name = 'operacoes.html'

    def get_context_data(self, **kwargs):
        context = super(OperacoesView, self).get_context_data(**kwargs)
        if self.request.GET:
            form = OperacoesListForm(self.request.GET)
        else:
            form = OperacoesListForm()
        context['form'] = form
        return context

    def get_queryset(self):
        qs = super(OperacoesView, self).get_queryset()
        if self.request.GET:
            form = OperacoesListForm(self.request.GET)
            if form.is_valid():
                desastre = form.cleaned_data['desastre']
                ong = form.cleaned_data['ong']
                if desastre:
                    qs = qs.filter(desastre=desastre)
                if ong:
                    qs = qs.filter(ong=ong)
        if qs.count()>0:
            paginator = Paginator(qs, 10)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request,'Não existem operações cadastradoas!')



class OperacoesAddView( SuccessMessageMixin, CreateView):
    model = Operacoes
    form_class = OperacoesModelForm
    template_name = 'operacoes_form.html'
    success_url = reverse_lazy('operacoes')
    success_message = 'Operacoes cadastrado com sucesso!'

class OperacoesUpdateView( SuccessMessageMixin, UpdateView):
    model = Operacoes
    form_class = OperacoesModelForm
    template_name = 'operacoes_form.html'
    success_url = reverse_lazy('operacoes')
    success_message = 'Operacoes alterado com sucesso!'

class OperacoesDeleteView( SuccessMessageMixin, DeleteView):
    model = Operacoes
    template_name = 'operacoes_apagar.html'
    success_url = reverse_lazy('operacoes')
    success_message = 'Operacoes excluído com sucesso!'

