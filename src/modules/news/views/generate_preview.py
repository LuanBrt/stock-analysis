from src.models import New
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from ..utils import get_description, get_image

# Cabeçalhos para a requisição HTTP
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
}

def generate_preview(request: HttpRequest, uuid: str) -> HttpResponse:
    """
    Gera uma prévia de uma notícia específica.

    Entrada:
        request (HttpRequest): Objeto de requisição HTTP que contém dados da solicitação.
        uuid (str): Identificador único da notícia.

    Saída:
        HttpResponse: Resposta HTTP que renderiza o template com a prévia da notícia.
    """
    new = New.objects.get(uuid=uuid)
    req = requests.get(new.url, headers)
    html = BeautifulSoup(req.content, 'html.parser')
    try:
        image = get_image(html)
        description = get_description(html)
    except Exception as e:
        image = None
        description = None
    if image is None:
        image = 'https://cdn-icons-png.flaticon.com/512/4149/4149706.png'
        description = ''
    context = {
       'new': new,
       'title': new.headline,
       'description': description,
       'image': image,
    }
    return render(request, 'portfolio/partials/new.html', context)
