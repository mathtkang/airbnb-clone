from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    # ~/users/login => 
    path("login", views.LoginView.as_view(), name="login"),
    #github
    # path("login/github", views.github_login, name="github-login"),
    # path("login/github/callback", views.github_callback, name="github-callback"),
    #kakao
    path("login/kakao", views.kakao_login, name="kakao-login"),
    path("login/kakao/callback", views.kakao_callback, name="kakao-callback"),
    #local
    path("logout", views.log_out, name="logout"),
    path("sigup", views.SignUpView.as_view(), name="signup"),
]