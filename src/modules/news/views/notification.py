from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

@login_required
def notification(request: HttpRequest) -> HttpResponse:
    """
    ENDPOINT para exibir notificações ao usuário.

    Entrada:
        request (HttpRequest): Objeto de requisição HTTP que contém dados da solicitação.

    Saída:
        HttpResponse: Resposta HTTP que renderiza o template com a mensagem de notificação.
    """
    return render(request, 'portfolio/partials/toast.html', {'message': request.GET['message'], 'type': request.GET['type']})
