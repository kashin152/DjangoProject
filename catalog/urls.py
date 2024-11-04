from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import (
    CatalogHomeView,
    CatalogContactsView,
    CatalogDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    ProductsByCategoryView,
    CategoryListView
)

app_name = "catalog"

urlpatterns = [
    path("home/", CatalogHomeView.as_view(), name="home"),
    path("contacts/", CatalogContactsView.as_view(), name="contacts"),
    path("product_detail/<int:pk>/", cache_page(60)(CatalogDetailView.as_view()), name="product_detail"),
    path("product_create/", ProductCreateView.as_view(), name="product_create"),
    path(
        "product_update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"
    ),
    path(
        "product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"
    ),
    path("category/<int:pk>/", ProductsByCategoryView.as_view(), name="products_by_category"),
    path("category_list/", CategoryListView.as_view(), name="category_list"),
]
