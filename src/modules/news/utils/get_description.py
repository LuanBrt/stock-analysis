from typing import Optional, Union
from bs4 import BeautifulSoup

def get_description(html: BeautifulSoup) -> Optional[Union[str, list]]:
    """
    Extrai a descrição da página HTML.

    Entrada:
        html (BeautifulSoup): Objeto BeautifulSoup que representa o conteúdo HTML da página.

    Saída:
        description (str ou None): Descrição extraída da página ou None se não encontrada.
    """
    description = None
    if html.find("meta", property="description"):
        description = html.find("meta", property="description").get('content')
    elif html.find("meta", property="og:description"):
        description = html.find("meta", property="og:description").get('content')
    elif html.find("meta", property="twitter:description"):
        description = html.find("meta", property="twitter:description").get('content')
    elif html.find("p"):
        description = html.find("p").contents
    return description
