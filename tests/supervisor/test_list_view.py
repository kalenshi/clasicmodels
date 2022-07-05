from django.urls import reverse
from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework import status

from api.employees.serializers import EmployeeSerializer
from api.supervisor.list_view import SupervisorsListView
from tests.factories.employee_factory import EmployeeFactory


class TestSupervisorListView(APITestCase):
    """
    Test the supervisor list view
    """

    def setUp(self) -> None:
        """
        Set up the necessary requirements for testing the list view
        """
        self.factory = APIRequestFactory()
        self.view = SupervisorsListView.as_view()
        self.serializer = EmployeeSerializer

    def test_get(self):
        """
        Test can retrieve a supervisor
        """
        supervisor = EmployeeFactory(reportsto=None)
        employees = EmployeeFactory.create_batch(6, reportsto=supervisor)

        request = self.factory.get(reverse("api:supervisors"))
        response = self.view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data[0]["manages"],
            [emp.pk for emp in employees]
        )
