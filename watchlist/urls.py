from django.urls import path

from .views import (PriceHistoryDetailView, PriceHistoryListView,
                    StockListView, StocksDetailView)

urlpatterns = [
    path('stock/', PriceHistoryListView.as_view()),
    path('stock/<int:pk>', PriceHistoryDetailView.as_view()),

]
