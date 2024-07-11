from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import get_top_products, get_product_details, ProductListView
from .api import ProductViewSet
from . import views

# Define router for ProductViewSet
router = DefaultRouter()
router.register(r'products', ProductViewSet)

# Define urlpatterns
urlpatterns = [
    path('top-products/', get_top_products, name='get_top_products'),  # Endpoint for top products
    path('product-details/<int:pk>/', get_product_details, name='get_product_details'),  # Endpoint for product details by product ID

    # Example endpoint for ProductListView
    path('products/', ProductListView.as_view(), name='product-list'),
    
    # API endpoints for top products and product details
    path('api/top-products/<str:category>/', views.get_top_products, name='get_top_products_by_category'),
    path('api/product-details/<str:category>/<int:product_id>/', views.get_product_details, name='get_product_details_by_category'),

    # Endpoint for fetching filtered products
    path('companies/<str:companyname>/categories/<str:categoryname>/products/', views.fetch_filtered_products, name='fetch_filtered_products'),
]
