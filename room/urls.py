from .views      import (
    DetailView,
    TradeHistoryView,
    NearInfoView,
    RoomListView,
    ClusterRoomListView,
    RoomUploadView
)

from django.urls import path

urlpatterns = [
    path('/detail', DetailView.as_view()),
    path('/trade-history', TradeHistoryView.as_view()),
    path('/near' , NearInfoView.as_view()),
    path('/upload', RoomUploadView.as_view()),
    path('/list' ,RoomListView.as_view()),
    path('/cluster', ClusterRoomListView.as_view()),
]
