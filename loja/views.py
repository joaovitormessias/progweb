# loja/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Produto
import django_filters
from .filters import ProdutoFilter
from django.contrib.auth.decorators import login_required
# CORREÇÃO: Importando 'messages' de uma forma segura para evitar conflitos
from django.contrib.messages import api as messages_api

# ----- Class-Based View para lista -----
class ListaProdutosView(ListView):
    model = Produto
    template_name = 'lista_produtos.html'
    context_object_name = 'produtos'

# ----- Class-Based View para detalhe -----
class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'produto_detail.html'
    context_object_name = 'produto'

def lista_produtos_filtrada(request):
    f = ProdutoFilter(request.GET, queryset=Produto.objects.all())
    return render(request, 'lista_produtos_filtrada.html', {'filter': f})


