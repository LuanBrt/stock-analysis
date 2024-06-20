from django.contrib import admin
from .models import New, Stock

# Registro dos modelos(models).
admin.site.register(Stock)
admin.site.register(New)