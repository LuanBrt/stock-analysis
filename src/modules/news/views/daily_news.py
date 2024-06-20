from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.utils.timezone import make_aware
from datetime import timedelta, datetime
from django.http import HttpRequest, HttpResponse
from src.models import Stock

@login_required
def daily_news(request: HttpRequest, uuid: str) -> HttpResponse:
    """
    ENDPOINT para exibir as notícias diárias de uma ação específica.

    Entrada:
        request (HttpRequest): Objeto de requisição HTTP que contém dados da solicitação.
        uuid (str): Identificador único da ação.

    Saída:
        HttpResponse: Resposta HTTP que renderiza o template com as notícias diárias da ação.
    """
    stock = get_object_or_404(Stock, uuid=uuid)
    if 'day' in request.GET.keys():
        day = float(request.GET['day'])
        day = make_aware(datetime.fromtimestamp(day))
    else:
        day = timezone.now()

    yesterday = day - timedelta(days=1)
    tomorrow = day + timedelta(days=1)

    news = stock.get_news().filter(pubdate__year=day.year, pubdate__month=day.month, pubdate__day=day.day)
    return render(request, 'portfolio/partials/day-newsletter.html', {'stock': stock, 'news': news, 'day': day, 'yesterday': yesterday.timestamp(), 'tomorrow': tomorrow.timestamp()})
