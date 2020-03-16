from .views      import DetailView, TradeHistoryView

from django.urls import path

urlpatterns = [
    path('/detail', DetailView.as_view()),
    path('/trade-history', TradeHistoryView.as_view()),
]
