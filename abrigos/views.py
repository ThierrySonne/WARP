from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import AbrigoModelForm
from .models import Abrigo

class AbrigosView(PermissionRequiredMixin, ListView):
    permission_required = 'abrigos.view_abrigo'
    permission_denied_message = 'Vizualizar Abrigos'
    model = Abrigo
    template_name = 'abrigos.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(AbrigosView, self).get_queryset()
        if buscar:
            return qs.filter(nome__icontains=buscar)

        if qs.count() > 0:
            paginator = Paginator(qs, 100)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request,'Não existem Abrigos')


class AbrigoAddView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = 'abrigos.add_abrigo'
    permission_denied_message = 'Adicionar Abrigos'
    model = Abrigo
    form_class = AbrigoModelForm
    template_name = 'abrigo_form.html'
    success_url = reverse_lazy('abrigos')
    success_message = 'Abrigo Adicionado com Sucesso!'

class AbrigoUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = 'abrigos.change_abrigo'
    permission_denied_message = 'Editar Abrigos'
    model = Abrigo
    form_class = AbrigoModelForm
    template_name = 'abrigo_form.html'
    success_url = reverse_lazy('abrigos')
    success_message = 'Abrigo atulizado com Sucesso!'

class AbrigoDeleteView(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    permission_required = 'abrigos.delete_abrigo'
    permission_denied_message = 'Eliminar Abrigos'
    model = Abrigo
    template_name = 'abrigo_apagar.html'
    success_url = reverse_lazy('abrigos')
    success_message = 'Abrigo apagado com Sucesso!'