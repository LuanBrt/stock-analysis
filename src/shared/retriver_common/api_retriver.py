import time
import requests
from celery.utils.log import get_task_logger
from .retriver_interface import RetriverInterface

# Celery Logger
logger = get_task_logger(__name__)

class ApiRetriver(RetriverInterface):
    def set_header(self):
        """
        Define a URL base e os cabeçalhos para as requisições da API.
        """
        self.__base_url = 'https://api-inference.huggingface.co/models/ProsusAI/finbert'
        self.__headers = {'Authorization': f'Bearer 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'}

    def query(self, payload: dict) -> float:
        """
        Faz uma consulta à API de análise de sentimento com o payload fornecido.

        Args:
            payload (dict): Os dados a serem enviados para a API de análise de sentimento.

        Returns:
            float: A pontuação de sentimento onde valores positivos indicam sentimento positivo e valores negativos indicam sentimento negativo.
        
        A função tenta enviar o payload para a API de análise de sentimento, trata as tentativas em caso de falhas,
        e processa a resposta para calcular uma pontuação de sentimento. Ela lida com limitações de taxa e outros erros de forma adequada.
        """
        retries = 0
        finished = False

        while not finished:
            retries += 1
            time.sleep(30)
            try:
                response = requests.post(self.__base_url, headers=self.__headers, json=payload).json()
            except Exception as e:
                logger.error(f"{e} na tentativa {retries}")
                retries += 1
                time.sleep(2 * (2 ** (retries - 1)))
            else:
                logger.error(f"{response} na tentativa {retries}")
                if isinstance(response, dict):
                    if 'error' in response.keys():
                        if 'estimated_time' in response.keys():
                            time.sleep(response['estimated_time'] * 2)
                        if 'RATE LIMIT REACHED' in response['error']:
                            time.sleep(60 * 60)
                elif isinstance(response, list):
                    finished = True

        output = response[0]
        score = 0
        for sentiment in output:
            if sentiment['label'] == 'positive':
                score += sentiment['score']
            if sentiment['label'] == 'negative':
                score -= sentiment['score']
        time.sleep(5)
        return score
