from django.views.generic import TemplateView
from .models import Apartament


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        context['apartament'] = Apartament.objects.all()

        return context


class ClientesView(TemplateView):
    template_name = 'clientes.html'
