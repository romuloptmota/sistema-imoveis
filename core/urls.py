from django.urls import path
from .views import IndexView, ClientesView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('clientes', ClientesView.as_view(), name='clientes')
]
