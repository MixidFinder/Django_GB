from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("products/last", views.last_products, name="last_products"),
    path("products/add", views.add_product, name="add_product"),
]
