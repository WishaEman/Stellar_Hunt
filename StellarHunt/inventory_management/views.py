from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.pagination import LimitOffsetPagination

from .serializers import (Category, CategorySerializer, Product,
                          ProductSerializer, Subcategory,
                          SubcategorySerializer)


class CategoryListView(generics.ListAPIView):
    """ API view to list categories with AllowAny permission. """

    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class SubcategoryListView(generics.ListAPIView):
    """ API view to list subcategories within a category. """

    serializer_class = SubcategorySerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Subcategory.objects.filter(category_id=category_id)


class ProductListView(generics.ListAPIView):
    """ API view to list products with AllowAny permission. """

    queryset = Product.objects.all().order_by('subcategory_id')
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]


class LatestProducts(generics.ListAPIView):
    """  API view to list the latest products with AllowAny permission. """

    queryset = Product.objects.order_by('created_at')[:9]
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]


class CategoryProductsAPIView(generics.ListAPIView):
    """ API view to list products within a subcategory using pagination. """

    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        subcategory_id = self.kwargs['subcategory_id']
        return Product.objects.filter(subcategory_id=subcategory_id)
