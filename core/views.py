from django.views.generic import TemplateView, ListView
from .models import Apartamento, Edificio

# controle de login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# login e registro
from django.shortcuts import render
from django.contrib.auth.models import User


class IndexListView(ListView):

    # Paginação
    template_name = 'index.html'
    paginate_by = 12
    ordering = '-edificio'
    model = Apartamento

    def get_queryset(self):

        # Campo de busca e return banco
        txt_nome = self.request.GET.get('nome')
        if txt_nome:
            edificios = Apartamento.objects.filter(disponivel=True, edificio__edificio=txt_nome)
        else:
            edificios = Apartamento.objects.filter(disponivel=True)

        return edificios


class ClientesView(LoginRequiredMixin, TemplateView):
    # acesso somente logado - deslogado enviado para index - LoginRequiredMixin
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
