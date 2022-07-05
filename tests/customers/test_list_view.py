from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory

from api.customers.list_view import CustomersListView
from api.customers.serializers import CustomerSerializer
from api.models import Customers
from tests.factories.customer_factory import CustomersFactory


class TestCustomersListView(APITestCase):
    """
    Class for testing the customers list view
    """

    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.view = CustomersListView.as_view()
        self.serializer = CustomerSerializer()

    def test_get_customers(self):
        """
        Test the endpoint retrieves and gives customer entries from the database
        """
        _ = CustomersFactory.create_batch(10)

        request = self.factory.get(reverse("api:customers"))
        response = self.view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["count"],
            Customers.objects.all().count()
        )
