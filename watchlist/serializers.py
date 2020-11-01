from rest_framework import serializers

from .models import PredictionModel, PriceHistory, Stocks, Watchlist


class StocksSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Stocks
        fields = '__all__'
        

class PriceHistory(serializers.ModelSerializer):

    class Meta:
        model = PriceHistory
        fields = '__all__'


class Watchlist(serializers.ModelSerializer):

    class Meta:
        model = Watchlist
        fields = '__all__'

        

