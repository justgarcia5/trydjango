from django.urls import path

from pages.views import home_view, contact_view, about_view
from products.views import (
    product_detail_view,
    product_create_view,
    product_update_view,
    product_detail_view,
    product_delete_view,
    product_list_view
)
app_name = 'products'
urlpatterns = [
    path('', product_list_view, name='product-list'),
    path('create/', product_create_view, name='product-create'),
    path('<int:id>/', product_detail_view, name='product-detail'),
    path('<int:id>/delete', product_delete_view, name='product-delete'),
    path('edit/<int:id>/', product_update_view, name='product-edit'),
]
