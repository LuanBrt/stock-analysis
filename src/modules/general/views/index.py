from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

@login_required
def index(request: HttpRequest) -> HttpResponse:
    """
    ENDPOINT para a página inicial do usuário.

    Entrada:
        request (HttpRequest): Objeto de requisição HTTP que contém dados da solicitação.

    Saída:
        HttpResponse: Resposta HTTP que renderiza a página inicial do portfólio com o contexto atualizado.
    """
    context = {}
    if 'timestamp' in request.GET.keys():
        context['timestamp'] = request.GET['timestamp']
    
    return render(request, 'portfolio/index.html', context)
