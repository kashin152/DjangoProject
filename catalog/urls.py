from django.urls import path
from catalog import views

urlpatterns = [
    path("home/", views.about, name="home"),
    path("contact/", views.contact, name="contact"),
]
