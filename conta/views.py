from django.shortcuts import render, redirect
from .forms import RegistroForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages


def registrar(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            novo_usuario = form.save(commit=False)
            novo_usuario.set_password(form.cleaned_data['password'])
            novo_usuario.save()
            return render(request, 'registro_concluido.html', {'novo_usuario': novo_usuario})
    else:
        form = RegistroForm

    return render(request, 'registrar.html', {'form': form})

@login_required
def minha_conta(request):
    return render(request, 'minha_conta.html')

@login_required
def excluir_conta(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()
        messages.sucess(request, 'Sua conta foi excluída com sucesso.')
        return redirect('lista_produtos')
    
    return render(request, 'excluir_conta_confirm.html')