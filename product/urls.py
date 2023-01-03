from django.urls import path

from product.views import ProductView,CategoryView


urlpatterns = [
    path("", ProductView.as_view(), name="products"),
    path("categories/", CategoryView.as_view(), name="product"),
]
