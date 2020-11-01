from rest_framework import serializers
from .models import Stocks, PriceHistory, PredictionModel


class StocksSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Stocks
        fields = '__all__'
        

class PriceHistory(serializers.ModelSerializer):

    class Meta:
        model = PriceHistory
        fields = '__all__'

