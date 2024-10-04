from django.urls import path
from catalog import views
from catalog.views import CatalogHomeView, CatalogContactsView, CatalogDetailView

urlpatterns = [
    path("home/", CatalogHomeView.as_view(), name="home"),
    path("contact/", CatalogContactsView.as_view(), name="contact"),
    path(
        "product_detail/<int:product_id>", CatalogDetailView.as_view(), name="product_detail"
    ),
]
