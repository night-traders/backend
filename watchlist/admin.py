from django.contrib import admin

from .models import PredictionModel, PriceHistory, Stocks, Watchlist

admin.site.register(Stocks)
admin.site.register(PriceHistory)
admin.site.register(Watchlist)

