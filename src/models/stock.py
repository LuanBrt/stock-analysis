import datetime
from django.utils import timezone
from django.conf import settings
from django.db import models
from typing import Type, Union
from .base_model import BaseModel

# Modelo que representa uma ação de uma empresa.
class Stock(BaseModel):
    ticker = models.CharField(max_length=50, unique=True)
    company = models.CharField(max_length=600)
    exchange = models.CharField(max_length=200)
    subscripted_users = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def get_news_in_interval(self, interval: str) -> Type[models.QuerySet]:
        """
        Retorna notícias em um intervalo de tempo específico.
        
        Args:
            interval (str): O intervalo de tempo para filtrar as notícias ('day' ou 'month').

        Returns:
            QuerySet: Um conjunto de notícias filtradas pelo intervalo de tempo especificado.
        """
        today = timezone.now()
        if interval == 'day':
            last = today - datetime.timedelta(days=1)
            return self.new_set.filter(pubdate__range=(last, today))
        elif interval == 'month':
            last = today - datetime.timedelta(days=30)
            return self.new_set.filter(pubdate__range=(last, today))

    def get_sentiment_value(self, interval: str) -> float:
        """
        Calcula o valor médio de sentimento das notícias em um intervalo de tempo específico.

        Args:
            interval (str): O intervalo de tempo para filtrar as notícias ('day' ou 'month').

        Returns:
            float: O valor médio de sentimento das notícias filtradas. Retorna 0 se não houver notícias.
        """
        news= self.get_news_in_interval(interval)
        if len(news) <= 0:
            return 0

        ratio= len(news)
        return sum(news.values_list('prediction', flat=True)) / ratio

    def get_news(self) -> Type[models.QuerySet]:
        """
        Retorna todas as notícias relacionadas à ação, ordenadas por data de publicação.

        Returns:
            QuerySet: Um conjunto de todas as notícias ordenadas por data de publicação.
        """
        news = self.new_set.order_by('-pubdate')
        return news
