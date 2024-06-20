from bs4 import BeautifulSoup
from typing import Optional

def get_image(html: BeautifulSoup) -> Optional[str]:
    """
    Extrai a imagem de compartilhamento da página HTML.

    Entrada:
        html (BeautifulSoup): Objeto BeautifulSoup que representa o conteúdo HTML da página.

    Saída:
        image (str ou None): URL da imagem extraída da página ou None se não encontrada.
    """
    image = None
    if html.find("meta", property="image"):
        image = html.find("meta", property="image").get('content')
    elif html.find("meta", property="og:image"):
        image = html.find("meta", property="og:image").get('content')
    elif html.find("meta", property="twitter:image"):
        image = html.find("meta", property="twitter:image").get('content')
    elif html.find("img", src=True):
        image = html.find_all("img").get('src')
    return image
