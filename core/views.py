from django.views.generic import TemplateView
from .models import Apartamento

# controle de login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        context['apartamento'] = Apartamento.objects.filter(disponivel=True)

        return context


class ClientesView(LoginRequiredMixin, TemplateView):
    #acesso somente logado - deslogado enviado para index
    login_url = reverse_lazy('index')

    template_name = 'clientes.html'

    def get_context_data(self, **kwargs):
        context = super(ClientesView, self).get_context_data(**kwargs)

        context['apartamento'] = Apartamento.objects.filter(disponivel=False)

        return context
