from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpRequest, HttpResponse
from src.models import Stock

@login_required
def add_stock(request: HttpRequest, uuid: str) -> HttpResponse:
    """
    ENDPOINT para adicionar um usuário autenticado à lista de usuários inscritos de uma ação.

    Entrada:
        request (HttpRequest): Objeto de requisição HTTP que contém dados da solicitação.
        uuid (str): Identificador único da ação.

    Saída:
        HttpResponse: Resposta HTTP que aciona a recarga das ações subscritas no frontend.
    """
    stock = get_object_or_404(Stock, uuid=uuid)
    stock.subscripted_users.add(request.user)

    response = HttpResponse()
    response['HX-Trigger'] = 'reloadstocks'
    response['HX-Reswap'] = 'none'
    return response
