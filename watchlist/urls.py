from django.urls import path
from .views import StockListView, StocksDetailView


urlpatterns = [
    path('', StockListView.as_view()),
    path('api/watchlist/<pk>', StocksDetailView.as_view()),

]