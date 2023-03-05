from django.views.generic import TemplateView
from .models import Apartamento

# controle de login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# login e registro
from django.shortcuts import render
from django.contrib.auth.models import User


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        context['apartamento'] = Apartamento.objects.filter(disponivel=True)

        return context


class ClientesView(LoginRequiredMixin, TemplateView):
    # acesso somente logado - deslogado enviado para index
    login_url = reverse_lazy('index')

    template_name = 'clientes.html'

    def get_context_data(self, **kwargs):
        context = super(ClientesView, self).get_context_data(**kwargs)

        context['apartamento'] = Apartamento.objects.filter(disponivel=False)

        return context


# Formulario de cadastro de usuarios
def criar(request):
    return render(request, 'create.html')


# Inserção dos dados dos usuarios no banco
def banco(request):
    data = {}
    if(request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'Senha e confirmação de senha diferentes'
        data['class'] = 'alert-danger'
    else:
        user = User.objects.create_superuser(request.POST['name'], request.POST['email'], request.POST['password'])
        user.save()
        data['msg'] = 'Usuario cadastrado com sucesso'
        data['class'] = 'alert-success'
    return render(request, 'create.html', data)
