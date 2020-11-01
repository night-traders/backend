from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from .models import PredictionModel, PriceHistory, Stocks
from .serializers import StocksSerializer


class StockListView(ListCreateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Stocks.objects.all()
    serializer_class = StocksSerializer
    pagination_class = None


class StocksDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Stocks.objects.all()
    serializer_class = StocksSerializer


