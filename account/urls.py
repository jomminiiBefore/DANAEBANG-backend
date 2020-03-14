from django.urls import path
from .views      import (
    SignUpView,
    SignInView,
    KakaoLoginView,
)

urlpatterns = [
    path('/sign-up', SignUpView.as_view()),
    path('/sign-in', SignInView.as_view()),
    path('/kakao-login', KakaoLoginView.as_view()),
]