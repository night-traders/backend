from django.db import models
from django.contrib.auth.models import User

from account.models import UserAccount


class Stocks(models.Model):
    stock_id = models.CharField(max_length=5)
    company_name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.stock_id}, {self.company_name}'


class PriceHistory(models.Model):
    name = models.CharField(max_length=64)
    ticker = models.CharField(max_length=64)
    price_current = models.DecimalField(max_digits=12, decimal_places=2)
    price_open = models.DecimalField(max_digits=12, decimal_places=2)
    previous_close = models.DecimalField(max_digits=12, decimal_places=2)
    price_high = models.DecimalField(max_digits=12, decimal_places=2)
    price_low = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f'{self.ticker}, {self.name}'


class PredictionModel(models.Model):
    stock_name = models.ForeignKey(Stocks, on_delete=models.CASCADE)
    ticker_name = models.CharField(max_length=5)
    date = models.DateField()
    predicted_price_open = models.DecimalField(max_digits=12, decimal_places=2)
    predicted_price_close = models.DecimalField(max_digits=12, decimal_places=2)
    predicted_price_high = models.DecimalField(max_digits=12, decimal_places=2)
    predicted_price_low = models.DecimalField(max_digits=12, decimal_places=2)
    predicted_volume = models.DecimalField(max_digits=12, decimal_places=2)


class Watchlist(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, default='')
    stock = models.ForeignKey(PriceHistory, on_delete=models.CASCADE)
