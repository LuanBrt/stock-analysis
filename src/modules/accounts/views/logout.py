from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import logout as django_logout
from django.urls import reverse_lazy

def logout(request: HttpRequest) -> HttpResponse:
    """
    ENDPOINT para logout de usuário.

    Entrada:
        request (HttpRequest): Objeto de requisição HTTP que contém dados da solicitação.

    Saída:
        HttpResponse: Resposta HTTP que redireciona o usuário para a página de login após o logout.
    """
    django_logout(request)
    return redirect(reverse_lazy('login'))
