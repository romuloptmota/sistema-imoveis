from django.urls import path
from .views import IndexListView, ClientesView, criar, banco


urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('clientes', ClientesView.as_view(), name='clientes'),
    path('criar/', criar, name='criar'),
    path('banco/', banco),
]
