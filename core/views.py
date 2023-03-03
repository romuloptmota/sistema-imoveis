from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class ClientesView(TemplateView):
    template_name = 'clientes.html'
