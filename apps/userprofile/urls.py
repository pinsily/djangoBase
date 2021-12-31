from django.urls import path
from userprofile import views

app_name = "userprofile"

urlpatterns = [
    path("login/", views.login, name="login"),

]