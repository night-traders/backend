from django.urls import include, path

from .views import SignupView

urlpatterns = [
    path('signup', SignupView.as_view()),
    path('api/watchlist/', include('watchlist.urls')),
]
