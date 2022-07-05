from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory

from api.models import Products
from api.products.list_view import ProductsListView
from tests.factories.product_factory import ProductsFactory


class TestProductListView(APITestCase):
    """
    Test Products list view
    """

    def setUp(self) -> None:
        """
        Set up all the necessary requirements for test
        """
        self.view = ProductsListView.as_view()
        self.factory = APIRequestFactory()

    def test_get(self):
        """
        Test retrieving the office by officecode
        """
        _ = ProductsFactory.create_batch(10)
        request = self.factory.get("/api/?limit=10&offset=0")

        response = self.view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["total"], Products.objects.all().count())
