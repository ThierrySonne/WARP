from django.views.generic import ListView

from .models import Ong


class OngsView(ListView):
    model = Ong
    template_name = 'ongs.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(OngsView, self).get_queryset()
        if buscar:
            return qs.filter(nome__icontains=buscar)
        return qs