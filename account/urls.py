from django.urls import path
from .views      import (
    SignUpView,
    SignInView,
    KakaoLoginView,
    FacebookSignInView
)

urlpatterns = [
    path('/sign-up', SignUpView.as_view()),
    path('/sign-in', SignInView.as_view()),
    path('/kakao-login', KakaoLoginView.as_view()),
    path('/facebook-signin', FacebookSignInView.as_view())
]
