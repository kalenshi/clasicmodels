from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory

from api.customers.detail_view import CustomersDetailView
from api.customers.serializers import CustomerSerializer
from api.models import Customers
from tests.factories.customer_factory import CustomersFactory
from tests.factories.employee_factory import EmployeeFactory


class TestCustomersDetailView(APITestCase):
    """
    Class for testing the customers list view
    """

    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.view = CustomersDetailView.as_view()
        self.serializer = CustomerSerializer

    def test_get_customers_by_pk(self):
        """
        Test the endpoint retrieves and gives a customer entry from the database
        """
        sales_rep = EmployeeFactory()
        customer = CustomersFactory(salesrepemployeenumber=sales_rep)

        request = self.factory.get(reverse("api:customers"))
        response = self.view(request, cust_id=customer.pk)

        serializer = self.serializer(instance=customer)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["salesrepemployeenumber"],
            serializer.data["salesrepemployeenumber"]
        )
