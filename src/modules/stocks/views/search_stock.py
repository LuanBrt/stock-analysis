from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from src.models import Stock

@login_required
def search_stock(request):
    """
    ENDPOINT para buscar ações com base em um ticker fornecido pelo usuário.

    Entrada:
        request (HttpRequest): Objeto de requisição HTTP que contém dados da solicitação.

    Saída:
        HttpResponse: Resposta HTTP que renderiza o template com os resultados da busca.
    """
    query = request.POST['ticker'].upper()
    stocks = Stock.objects.filter(ticker__icontains=query)[:10]
    return render(request, 'portfolio/partials/search-stocks.html', {'stocks': stocks})
