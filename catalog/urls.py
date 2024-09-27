from django.urls import path
from catalog import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path(
        "product_detail/<int:product_id>", views.product_detail, name="product_detail"
    ),
]
