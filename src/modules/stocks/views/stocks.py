from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

@login_required
def stocks(request: HttpRequest) -> HttpResponse:
    """
    ENDPOINT para exibir as ações subscritas pelo usuário autenticado.

    Entrada:
        request (HttpRequest): Objeto de requisição HTTP que contém dados da solicitação.

    Saída:
        HttpResponse: Resposta HTTP que renderiza o template com a lista de ações subscritas e o timestamp.
    """
    stocks = request.user.stock_set.all()
    timestamp = 'day' if 'timestamp' not in request.GET.keys() else request.GET['timestamp']
    return render(request, 'portfolio/partials/stocks.html', {'stocks': stocks, 'timestamp': timestamp})
