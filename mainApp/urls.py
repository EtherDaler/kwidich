from .views import main, login_page, registration, logout_page
from django.urls import path


urlpatterns = [
    path("", main, name="main"),
    path("login/", login_page, name="login"),
    path("logout/", logout_page, name="logout"),
    path("registration/", registration, name="registration")
]