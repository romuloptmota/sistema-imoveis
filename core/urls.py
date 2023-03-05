from django.urls import path
from .views import IndexView, ClientesView, criar, banco


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('clientes', ClientesView.as_view(), name='clientes'),
    path('criar/', criar),
    path('banco/', banco),
]
