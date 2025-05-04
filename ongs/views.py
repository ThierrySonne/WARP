from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import OngModelForm
from .models import Ong


class OngsView(PermissionRequiredMixin, ListView):
    permission_required = "ongs.view_ong"
    permission_denied_message = 'Vizualizar ONGS'
    model = Ong
    template_name = 'ongs.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(OngsView, self).get_queryset()
        if buscar:
            return qs.filter(nome__icontains=buscar)

        if qs.count() > 0:
            paginator = Paginator(qs, 100)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, 'Não existem ONGs cadastradas!')

class OngAddView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = "ongs.add_ong"
    permission_denied_message = 'Adicionar ONGS'
    model = Ong
    form_class = OngModelForm
    template_name = 'ong_form.html'
    success_url = reverse_lazy('ongs')
    success_message = 'Ong cadastrada com sucesso!'

class OngUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = "ongs.change_ong"
    permission_denied_message = 'Editar ONGS'
    model = Ong
    form_class = OngModelForm
    template_name = 'ong_form.html'
    success_url = reverse_lazy('ongs')
    success_message = 'Ong atualizada com sucesso!'

class OngDeleteView(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    permission_required = "ongs.delete_ong"
    permission_denied_message = 'Eliminar ONGS'
    model = Ong
    template_name = 'ong_apagar.html'
    success_url = reverse_lazy('ongs')
    success_message = 'Ong apagada com sucesso!'