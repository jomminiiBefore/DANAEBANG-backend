from .views      import (
    DetailView,
    TradeHistoryView,
    NearInfoView,
    RoomListView,
    FilteredRoomListView,
    FilteredPositionListView,
    RoomUploadView,
    RoomLikeView
)

from django.urls import path

urlpatterns = [
    path('/detail', DetailView.as_view()),
    path('/trade-history', TradeHistoryView.as_view()),
    path('/near' , NearInfoView.as_view()),
    path('/upload', RoomUploadView.as_view()),
    path('/list' ,FilteredRoomListView.as_view()),
    path('/click', RoomListView.as_view()),
    path('/map', FilteredPositionListView.as_view()),
    path('/like', RoomLikeView.as_view()),
]