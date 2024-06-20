import csv
import os
import time
from django.conf import settings
from src.shared.retriver_common.news_retriver import NewsRetriver
from celery.utils.log import get_task_logger
from datetime import timedelta
from django.utils import timezone
from urllib.error import HTTPError
from celery import shared_task
from src.models import Stock, New
from src.shared.retriver_common.api_retriver import ApiRetriver
from celery import Task

logger = get_task_logger(__name__)

# Variáveis Globais
CONNECTION_TIMEOUT: int = 20

@shared_task(bind=True, name='stock_creation')
def get_data_for_stocks(self: Task) -> None:
    """
    Tarefa Celery para obter dados de ações e criar instâncias no banco de dados.

    Entrada:
        self (Task): Instância da tarefa Celery.

    Saída:
        None
    """
    file_path: str = os.path.join(settings.BASE_DIR, 'data/us_symbols.csv')
    logger.info("going to get data")

    api_retriver = ApiRetriver()
    api_retriver.set_header()
    scrapper = NewsRetriver()
    scrapper.set_header()

    with open(file_path, 'r') as file:
        dt = csv.reader(file, delimiter=',')
        for stock in dt:
            news = None
            if stock[2] not in ['NYSE', 'NASDAQ']:
                continue
            if Stock.objects.filter(ticker=stock[0]).exists():
                continue
            stock_instance = Stock.objects.create(ticker=stock[0], company=stock[1], exchange=stock[2])
            
            connection_count: int = 0
            while news is None and connection_count <= CONNECTION_TIMEOUT:
                try:
                    news = scrapper.query({'ticker': stock[0]})

                except Exception as e:

                    if isinstance(e, HTTPError):
                        if e.code == 404:
                            # página não existe: excluir ticker
                            stock_instance.delete()
                            connection_count = CONNECTION_TIMEOUT
                    logger.error(e)
                    time.sleep(1)
                    connection_count += 1
                else:
                    for new in news:
                        time.sleep(2)
                        New.objects.create(
                            stock=stock_instance, 
                            headline=new['headline'], 
                            url=new['url'], 
                            pubdate=new['pubdate'], 
                            prediction=api_retriver.query({'inputs': new['headline'], 'options': {'wait_for_model': True}})
                        )

@shared_task(bind=True)
def update_news(self: Task) -> None:
    """
    Tarefa Celery para atualizar as notícias relacionadas às ações.

    Entrada:
        self (Task): Instância da tarefa Celery.

    Saída:
        None
    """
    stocks = Stock.objects.all()
    api_retriver = ApiRetriver()
    api_retriver.set_header()
    scrapper = NewsRetriver()
    scrapper.set_header()

    for stock in stocks:
        news = scrapper.query({'ticker': stock.ticker})

        for new in news:
            if not New.objects.filter(headline=new['headline']).exists():
                sentiment_value = api_retriver.query({'inputs': new['headline'], 'options': {'wait_for_model': True}})
                New.objects.create(
                    headline=new['headline'], 
                    pubdate=new['pubdate'], 
                    prediction=sentiment_value, 
                    url=new['url'], 
                    stock=stock
                )

@shared_task(bind=True)
def clean_old_news(self: Task) -> None:
    """
    Tarefa Celery para limpar notícias antigas (mais de um mês) do banco de dados.

    Entrada:
        self (Task): Instância da tarefa Celery.

    Saída:
        None
    """
    news = New.objects.all()
    for new in news:
        if new.date < (timezone.now() - timedelta(days=30)):
            new.delete()
