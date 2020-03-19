from django.urls import path
from .views      import (
    SignUpView,
    SignInView,
    KakaoSignInView,
    FacebookSignInView,
    AuthSMSView,
    AuthSMSConfirmView
)

urlpatterns = [
    path('/sign-up', SignUpView.as_view()),
    path('/sign-in', SignInView.as_view()),
    path('/kakao-signin', KakaoSignInView.as_view()),
    path('/facebook-signin', FacebookSignInView.as_view()),
    path('/auth-mobile', AuthSMSView.as_view()),
    path('/mobile-confirm', AuthSMSConfirmView.as_view())
]
