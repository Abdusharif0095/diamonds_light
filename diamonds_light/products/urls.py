from django.urls import path, include
from .views import AddProduct, GetCategory, GetProduct

urlpatterns = [
    path('add/', AddProduct.as_view(), name='add_product'),
    path('category/<int:category_id>/<slug:category_slug>/', GetCategory.as_view(), name='get_category'),
    path('product/<int:product_id>/<slug:slug>', GetProduct.as_view(), name='get_product'),
]
