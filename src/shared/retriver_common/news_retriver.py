from typing import Dict, List
from urllib.request import urlopen, Request
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from django.utils import timezone
from django.utils.timezone import make_aware
from dateutil import parser
from .retriver_interface import RetriverInterface
from celery.utils.log import get_task_logger

# Celery Logger
logger = get_task_logger(__name__)

class NewsRetriver(RetriverInterface):
    def set_header(self):
        """
        Sets the base URL and headers for the web scraper.
        """
        self.__base_url = 'https://finviz.com/quote.ashx?t='
        self.__headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
        }
        
    def query(self, payload: dict) -> List[Dict[str, str]]:
        """
        Scrapes recent news articles for the given stock ticker.

        Args:
            payload (dict): A dictionary containing the stock ticker symbol with the key 'ticker'.

        Returns:
            List[Dict[str, str]]: A list of dictionaries containing news articles with publication date,
                                  headline, and URL.
        
        The function fetches the news articles from Finviz for the specified stock ticker, extracts the news
        headlines, publication dates, and URLs, and returns them as a list of dictionaries. Only the news
        articles published within the last 30 days are included in the results.
        """
        news = []
        url = self.__base_url + payload['ticker']
        response = urlopen(Request(url=url, headers=self.__headers))
        html = BeautifulSoup(response, 'html.parser')
        news_html = html.find(id='news-table')
        
        for row in news_html.find_all('tr'):
            title = row.a.get_text()
            link = row.a['href']
            scrapped_date = row.td.text.split()
            time_str = scrapped_date[-1]
            if len(scrapped_date) > 1:
                date_str = scrapped_date[0]
            else:
                date_str = timezone.now().strftime('%b-%d-%y')
            try:
                date = make_aware(parser.parse(f"{date_str} {time_str}"))
            except ValueError as e:
                logger.error(f"Error parsing date: {e}")
                # Default to current time if parsing fails
                date = timezone.now()
            
            if date > (timezone.now() - timedelta(days=30)):
                news.append({'pubdate': date, 'headline': title, 'url': link})

        return news