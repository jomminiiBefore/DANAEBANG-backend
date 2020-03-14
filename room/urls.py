from .views      import DetailView, TradeHistoryView, NearInfoView

from django.urls import path

urlpatterns = [
    path('/detail', DetailView.as_view()),
    path('/trade-history', TradeHistoryView.as_view()),
    path('/near' , NearInfoView.as_view()),
]
