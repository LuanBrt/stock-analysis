from django.shortcuts import render, redirect
from django.contrib.auth import login
from ..utils import RegistrationForm
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy

def register(request: HttpRequest) -> HttpResponse:
    """
    ENDPOINT para registro de usuário.

    Entrada:
        request (HttpRequest): Objeto de requisição HTTP que contém dados da solicitação.

    Saída:
        HttpResponse: Resposta HTTP que redireciona o usuário para a página inicial após o registro e login bem-sucedidos,
                      ou se der error re-renderiza a página de registro com o formulário.
    """
    form = RegistrationForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse_lazy('index'))
        return render(request, 'accounts/register.html', {'form': form, 'title': 'Register'})

    return render(request, 'accounts/register.html', {'form': RegistrationForm(), 'title': 'Register'})
