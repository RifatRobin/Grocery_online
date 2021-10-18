from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path("login", views.login, name="login_page"),
    path("signup", views.signup, name="signup_page"),
    path("", views.home, name="home_page"),
    path("logout", views.logout, name="logout_page"),

    # this is for the viwing process of a particular product
    path("preview/<int:product_id>", views.product_preview, name="preview_page"),
   
]
