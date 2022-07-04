from rest_framework.test import APITestCase

from tests.factories.product_factory import ProductsFactory


class TestProductModel(APITestCase):
    """
    Test the product model's string function
    """

    def setUp(self) -> None:
        """
        Create a product instance
        """
        self.product = ProductsFactory(productcode="XX-10")

    def test_string_representation(self):
        self.assertEqual(self.product.__str__(), "Product-XX-10")
