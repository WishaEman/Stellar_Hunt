from django.urls import path

from .views import (CategoryListView, CategoryProductsAPIView,
                    CategoryRetrieveView, ProductListView, LatestProducts,
                    ProductViewSet, SubcategoryListView)

app_name = 'inventory_management'

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryRetrieveView.as_view(), name='category'),
    path('subcategories/<int:category_id>/', SubcategoryListView.as_view(), name='subcategory-list'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('latest-products/', LatestProducts.as_view(), name='latest-product'),
    path('categories/<int:subcategory_id>/products/', CategoryProductsAPIView.as_view(), name='category-products'),
    path('products/by-category/', ProductViewSet.as_view({'get': 'by_category'}), name='product-list-by-category'),
]

