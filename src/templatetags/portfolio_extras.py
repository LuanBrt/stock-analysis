from __future__ import absolute_import, unicode_literals
from django import template
from src.models import Stock

register: template.Library = template.Library()

@register.filter
def get_timestamp_news(stock: Stock, timestamp: str) -> int:
    """
    Filtro de template para obter o número de notícias de uma ação em um intervalo de tempo específico.

    Entrada:
        stock (Stock): Objeto da ação.
        timestamp (str): Intervalo de tempo ('day', 'month', etc.).

    Saída:
        int: Número de notícias no intervalo de tempo especificado.
    """
    return len(stock.get_news_in_interval(timestamp))

@register.filter
def get_sentiment_value(stock: Stock, timestamp: str) -> float:
    """
    Filtro de template para obter o valor de sentimento das notícias de uma ação em um intervalo de tempo específico.

    Entrada:
        stock (Stock): Objeto da ação.
        timestamp (str): Intervalo de tempo ('day', 'month', etc.).

    Saída:
        float: Valor de sentimento no intervalo de tempo especificado.
    """
    return stock.get_sentiment_value(timestamp)
