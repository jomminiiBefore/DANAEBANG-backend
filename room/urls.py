from .views      import DetailView

from django.urls import path

urlpatterns = [
    path('/detail', DetailView.as_view()),
]
