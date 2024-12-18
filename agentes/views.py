from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.shortcuts import redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.views.generic.base import TemplateResponseMixin

from WARP import settings
from .forms import AgenteModelForm, AgenteMissaoInLine
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


    def enviar_email(self, agente):
        email =[]
        email.append(agente.email)

        dados = {'agente': agente.nome,
                 'ong': agente.ong, }

        texto_email = render_to_string('emails/texto_email.txt', dados)
        html_email = render_to_string('emails/texto_email.html', dados)
        send_mail(subject='WARP, Alistamento concluído',
                  message=texto_email,
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=email,
                  html_message=html_email,
                  fail_silently=False,
                  )
        self.enviar_email(agente)
        return redirect('agentes')

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

class AgenteInLineEditView(TemplateResponseMixin, View):
    template_name = 'agente_form_inline.html'


    def get_formset(self, data=None):
        return AgenteMissaoInLine(instance=self.agente, data=data)

    def dispatch(self, request, pk):
        self.agente = get_object_or_404(Agente, pk=pk)
        return super().dispatch(request, pk)

    def get(self, request, *args, **kwargs):
        formset = self.get_formset()
        return self.render_to_response({'agente': self.agente, 'formset': formset})


    def post(self, request, *args, **kwargs):
        formset = self.get_formset(data=request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('agentes')
        return self.render_to_response({'agente': self.agente, 'formset': formset})
