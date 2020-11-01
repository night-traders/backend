from django.contrib import admin
from .models import Stocks, PriceHistory, PredictionModel


admin.site.register(Stocks)
admin.site.register(PriceHistory)

