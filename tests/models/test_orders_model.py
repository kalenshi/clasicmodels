from rest_framework.test import APITestCase

from tests.factories.customer_factory import CustomersFactory
from tests.factories.orders_factory import OrdersFactory


class TestOrdersModel(APITestCase):
    """
    Test the order model's string function
    """

    def setUp(self) -> None:
        """
        Create an order instance
        """
        self.customer = CustomersFactory(customernumber=10)
        self.order = OrdersFactory(ordernumber=10, customernumber=self.customer)

    def test_string_representation(self):
        self.assertEqual(self.order.__str__(), "Order-10")
