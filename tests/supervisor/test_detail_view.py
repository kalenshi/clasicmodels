from unittest.mock import patch

from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework import status

from api.employees.serializers import EmployeeSerializer
from api.supervisor.detail_view import SupervisorsDetailView
from tests.factories.employee_factory import EmployeeFactory


class TestSupervisorDetailView(APITestCase):
    """
    Test the supervisor detail view
    """

    def setUp(self) -> None:
        """
        Set up the necessary requirements for testing the detail view
        """
        self.factory = APIRequestFactory()
        self.view = SupervisorsDetailView.as_view()
        self.serializer = EmployeeSerializer

    def test_get_by_emp_no(self):
        """
        Test can retrieve a supervisor
        """
        supervisor = EmployeeFactory(employeenumber=1002, reportsto=None)
        employees = EmployeeFactory.create_batch(6, reportsto=supervisor)

        request = self.factory.get(reverse("api:supervisor_detail", args=("emp_no",)))
        response = self.view(request, emp_no=1002)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @patch("api.supervisor.detail_view.Employees")
    def test_supervisor_not_found(self, employee_patch):
        """
        Test that the supervisor requested for does not exist
        """
        employee_patch.objects.prefetch_related().get.side_effect = ObjectDoesNotExist
        with self.assertRaises(Exception) as ve:
            request = self.factory.get(
                reverse("api:supervisor_detail", args=("emp_no",))
            )
            _ = self.view(request, emp_no=100000)
        self.assertEqual(
            str(ve.exception),
            f"Employee with employeenumber 100000 Does not exist!"
        )
