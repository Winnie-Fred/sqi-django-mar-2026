from django.urls import path

from django.contrib.auth.views import LoginView, LogoutView

from . import views

app_name = "users"

urlpatterns = [
    path("sign-up/", views.sign_up, name="sign_up"),
    path("log-in/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("log-out/", LogoutView.as_view(), name="logout"),
]