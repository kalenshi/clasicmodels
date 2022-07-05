from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory

from api.products.detail_view import ProductsDetailView
from api.products.serializers import ProductsSerializer
from tests.factories.product_factory import ProductsFactory


class TestProductsDetailView(APITestCase):
    """
    Test Products list view
    """

    def setUp(self) -> None:
        """
        Set up all the necessary requirements for test
        """
        self.view = ProductsDetailView.as_view()
        self.factory = APIRequestFactory()
        self.serializer = ProductsSerializer()

    def test_get_by_id(self):
        """
        Test retrieving the office by officecode
        """
        product = ProductsFactory(productcode="XXX-10")
        request = self.factory.get("/api/products")

        response = self.view(request, product.pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
