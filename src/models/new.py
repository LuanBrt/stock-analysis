from django.db import models
from .base_model import BaseModel
from .stock import Stock

# Modelo que representa uma notícia associada a uma ação(stock).
class New(BaseModel):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    headline = models.CharField(max_length=900)
    prediction = models.FloatField()
    url = models.CharField(max_length=900)
    pubdate = models.DateTimeField()
