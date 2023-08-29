from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Category, Product, Subcategory


class InventoryManagementAPITestCase(APITestCase):
    """ Test case class for inventory management API views. """

    def setUp(self):
        self.category = Category.objects.create(title='TestCategory')
        self.subcategory = Subcategory.objects.create(title='TestSubcategory', category=self.category)
        self.product = Product.objects.create(title='TestProduct', subcategory=self.subcategory, price=10.99)

    def test_category_list(self):
        """ Test listing of categories using CategoryListView. """

        response = self.client.get(reverse('inventory_management:category-list'))
        self.assertEqual(
            response.data['results'],
            [{'id': self.category.id, 'title': 'TestCategory', 'description': ''}]
        )

    def test_subcategory_list(self):
        """ Test listing of subcategories within a category using SubcategoryListView. """

        response = self.client.get(reverse('inventory_management:subcategory-list', args=[self.category.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['results'],
            [{'id': self.subcategory.id, 'title': 'TestSubcategory', 'description': '', 'category': self.category.id}]
        )

    def test_product_list(self):
        """ Test listing of products using ProductListView. """

        response = self.client.get(reverse('inventory_management:product-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_latest_products(self):
        """ Test listing of latest products using LatestProducts view. """

        response = self.client.get(reverse('inventory_management:latest-product'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), Product.objects.count())

    def test_category_products(self):
        """ Test listing of products within a subcategory using CategoryProductsAPIView. """

        response = self.client.get(reverse('inventory_management:category-products', args=[self.subcategory.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), Product.objects.count())
