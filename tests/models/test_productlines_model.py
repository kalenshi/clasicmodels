from rest_framework.test import APITestCase

from tests.factories.productline_factory import ProductLinesFactory


class TestProductLinesModel(APITestCase):
    """
    Test the productlines model's string function
    """

    def setUp(self) -> None:
        """
        Create a productlines instance
        """
        self.productline = ProductLinesFactory()

    def test_string_representation(self):
        self.assertEqual(self.productline.__str__(), "ProductLine-XXXX-1")
