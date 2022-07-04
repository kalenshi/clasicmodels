from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase
from django.urls import reverse

from api.employees.list_view import EmployeesListView
from api.models import Employees
from tests.factories.employee_factory import EmployeeFactory
from tests.factories.office_factory import OfficesFactory


class TestEmployeeListView(APITestCase):
    """
    class for testing the employee list view
    """

    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.view = EmployeesListView.as_view()

    def test_get(self):
        """
        Test the get endpoint
        """
        _ = EmployeeFactory.create_batch(5)
        response = self.client.get(reverse("api:employees"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), Employees.objects.count())

    def test_post(self):
        """
        Test POSTing an employee works correctly
        """
        url = reverse("api:employees")
        supervisor = EmployeeFactory()
        office = OfficesFactory()
        employee_data = {
            "firstname": "kalenshi",
            "lastname": "katebe",
            "email": "test@email.com",
            "officecode": office.pk,
            "reportsto": supervisor.pk,
            "jobtitle": "Developer",
            "extension": "XXX"
        }
        response = self.client.post(url, employee_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
