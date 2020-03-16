from .views      import (
    DetailView, 
    TradeHistoryView, 
    NearInfoView,
    RoomUploadView
)

from django.urls import path

urlpatterns = [
    path('/detail', DetailView.as_view()),
    path('/trade-history', TradeHistoryView.as_view()),
    path('/near' , NearInfoView.as_view()),
    path('/upload', RoomUploadView.as_view()),
]