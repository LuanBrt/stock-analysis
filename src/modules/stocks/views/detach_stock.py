from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpRequest, HttpResponse
from src.models import Stock

@login_required
def detach_stock(request: HttpRequest, ticker: str) -> HttpResponse:
    """
    ENDPOINT para remover um usuário autenticado da lista de usuários subscritos de uma ação.

    Entrada:
        request (HttpRequest): Objeto de requisição HTTP que contém dados da solicitação.
        ticker (str): Ticker da ação.

    Saída:
        HttpResponse: Resposta HTTP que aciona a recarga das ações subscritas no frontend.
    """
    stock = get_object_or_404(Stock, ticker=ticker)
    stock.subscripted_users.remove(request.user)

    response = HttpResponse()
    response['HX-Trigger'] = 'reloadstocks'
    return response
