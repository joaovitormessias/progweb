# loja/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import Q, F
from django.db import transaction
from django.views.decorators.http import require_POST
from .models import Produto
from .filters import ProdutoFilter
from django.contrib.auth.decorators import login_required
# CORREÇÃO: Importando 'messages' de uma forma segura para evitar conflitos
from django.contrib.messages import api as messages_api
from carrinho.carrinho import Carrinho

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

@require_POST
def adicionar_ao_carrinho(request, produto_id):
    if not request.user.is_authenticated:
        # CORREÇÃO: Usando 'messages_api'
        messages_api.error(request, 'Você precisa estar logado para adicionar produtos ao carrinho.')
        return redirect('login')

    produto = get_object_or_404(Produto, id=produto_id)

    if not produto.disponivel or produto.quantidade <= 0:
        # CORREÇÃO: Usando 'messages_api'
        messages_api.error(request, f'Desculpe, o produto "{produto.nome}" não está mais disponível em estoque.')
        return redirect('lista_produtos')

    carrinho = Carrinho(request)
    carrinho.adicionar(produto=produto)
    # CORREÇÃO: Usando 'messages_api'
    messages_api.success(request, f'"{produto.nome}" foi adicionado ao seu carrinho!')
    return redirect('ver_carrinho')

@login_required
@require_POST
def remover_do_carrinho(request, produto_id):
    carrinho = Carrinho(request)
    produto = get_object_or_404(Produto, id=produto_id)
    carrinho.remover(produto)
    return redirect('ver_carrinho')

@login_required
def ver_carrinho(request):
    carrinho = Carrinho(request)
    return render(request, 'carrinho.html', {'carrinho': carrinho})

@login_required
@require_POST
def checkout(request):
    """Commit all stock decrements together; rollback on any unavailable item."""
    carrinho = Carrinho(request)
    try:
        with transaction.atomic():
            for product_id, item in carrinho.carrinho.items():
                quantity = item['quantidade']
                if quantity <= 0:
                    raise ValueError('Quantidade inválida.')
                # A conditional update prevents a stale read from overselling stock.
                updated = Produto.objects.filter(pk=product_id, disponivel=True, quantidade__gte=quantity).update(quantidade=F('quantidade') - quantity)
                if not updated:
                    raise ValueError('Um produto não tem estoque suficiente.')
                Produto.objects.filter(pk=product_id, quantidade=0).update(disponivel=False)
    except ValueError as error:
        messages_api.error(request, str(error))
        return redirect('ver_carrinho')
    carrinho.limpar()
    return render(request, 'checkout_concluido.html')
