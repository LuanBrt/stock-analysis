from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from src.models import Stock

@login_required
def stock(request: HttpRequest, ticker: str) -> HttpResponse:
    """
    ENDPOINT para exibir os detalhes de uma ação específica.

    Entrada:
        request (HttpRequest): Objeto de requisição HTTP que contém dados da solicitação.
        ticker (str): Ticker da ação.

    Saída:
        HttpResponse: Resposta HTTP que renderiza o template com os detalhes da ação.
    """
    stock = get_object_or_404(Stock, ticker=ticker)
    return render(request, 'portfolio/stock.html', {'stock': stock})
