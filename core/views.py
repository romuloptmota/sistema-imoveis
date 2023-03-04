from django.views.generic import TemplateView
from .models import Apartamento


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        context['apartamento'] = Apartamento.objects.filter(disponivel=True)

        return context


class ClientesView(TemplateView):
    template_name = 'clientes.html'

    def get_context_data(self, **kwargs):
        context = super(ClientesView, self).get_context_data(**kwargs)

        context['apartamento'] = Apartamento.objects.filter(disponivel=False)

        return context
