from django.http import HttpRequest, HttpResponse
from ..utils import LoginForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login

def login(request: HttpRequest) -> HttpResponse:
    """
    ENDPOINT para login de usuário.

    Entrada:
        request (HttpRequest): Objeto de requisição HTTP que contém dados da solicitação.

    Saída:
        HttpResponse: Resposta HTTP que redireciona o usuário para a página inicial se a autenticação for bem-sucedida,
                      ou se der erro re-renderiza a página de login com o formulário.
    """
    # Se  usuário já estiver cadastrado automaticamente é redirecionado para o portfolio
    if request.user.is_authenticated:
        return redirect(reverse_lazy('index'))

    form = LoginForm(request, data=request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            django_login(request, user)
            return redirect(reverse_lazy('index'))
        return render(request, 'accounts/login.html', {'form': form, 'title': 'Login'})

    return render(request, 'accounts/login.html', {'form': form, 'title': 'Login'})
