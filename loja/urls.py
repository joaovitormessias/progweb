# loja/urls.py
from django.urls import path
from .views import (
    ListaProdutosView, 
    ProdutoDetailView, 
    )

urlpatterns = [
    path('', ListaProdutosView.as_view(), name='lista_produtos'),
    path('produto/<int:pk>/', ProdutoDetailView.as_view(), name='produto_detail'),
    ]
