from django.contrib import admin
from django.urls import path
from .modules.general import index
from .modules.news import generate_preview, daily_news, notification
from .modules.stocks import stock, stocks, search_stock, add_stock, detach_stock
from .modules.accounts import login, register, logout

# Definição dos endpoints da aplicação
urlpatterns = [
    path('', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('portfolio/', index, name='index'),
    path('new/<str:uuid>', generate_preview, name='new-details'),
    path('news/<str:uuid>', daily_news, name='daily-news'),
    path('toast/', notification),
    path('stock/<str:ticker>', stock, name='stock'),
    path('stocks/', stocks, name='stocks'),
    path('stocks/search', search_stock, name='search-stock'),
    path('stock/add/<str:uuid>', add_stock, name='add-stock'),
    path('stock/detach/<str:ticker>', detach_stock, name='detach-stock'),
    path('admin/', admin.site.urls),
]
