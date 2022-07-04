from rest_framework.test import APITestCase

from tests.factories.customer_factory import CustomersFactory


class TestCustomerModel(APITestCase):
    """
    Test the customer model's string function
    """

    def setUp(self) -> None:
        """
        Create a customer instance
        """
        self.customer = CustomersFactory(customernumber=10)

    def test_string_representation(self):
        self.assertEqual(self.customer.__str__(), "Customer-10")
