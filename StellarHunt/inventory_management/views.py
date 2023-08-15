from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import (Category, CategorySerializer, Product,
                          ProductSerializer, Subcategory,
                          SubcategorySerializer)


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class SubcategoryListView(generics.ListAPIView):
    serializer_class = SubcategorySerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Subcategory.objects.filter(category_id=category_id)


class CategoryRetrieveView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all().order_by('subcategory_id')
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]


class LatestProducts(generics.ListAPIView):
    queryset = Product.objects.order_by('subcategory_id')[:10]
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]


class CategoryProductsAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        subcategory_id = self.kwargs['subcategory_id']
        return Product.objects.filter(subcategory_id=subcategory_id)


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['GET'])
    def by_category(self, request):
        category_name = request.query_params.get('category_name')
        if category_name:
            try:
                subcategory = Subcategory.objects.get(title=category_name)
                products = Product.objects.filter(subcategory=subcategory)
                serializer = self.get_serializer(products, many=True)
                return Response(serializer.data)
            except Category.DoesNotExist:
                return Response({'message': 'Category not found'}, status=404)
        return Response({'message': 'No category name provided'}, status=400)
