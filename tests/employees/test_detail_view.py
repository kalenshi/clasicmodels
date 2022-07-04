from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase

from api.employees.detail_view import EmployeesDetailView
from api.employees.serializers import EmployeeSerializer
from api.models import Employees
from tests.factories.employee_factory import EmployeeFactory


class TestEmployeeDetailView(APITestCase):
    """
    class for testing the employee detail view
    """

    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.view = EmployeesDetailView.as_view()
        self.serializer = EmployeeSerializer
        self.employee = EmployeeFactory(employeenumber=1008)

    def test_get_by_emp_no(self):
        """
        Test the get endpoint
        """

        request = self.factory.get("/api/employees/")
        response = self.view(request, emp_no=self.employee.pk)

        serializer = self.serializer(instance=Employees.objects.get(pk=1008))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_delete(self):
        """
        Test deleting an employee updates their active status to inactive
        """
        request = self.factory.delete("/api/employees/")
        response = self.view(request, emp_no=1008)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data["active"], 0)

    def test_patch(self):
        """
        Test patching an employee works
        """
        patch_data = {
            "firstname": "Kalenshi"
        }
        request = self.factory.patch(f"/api/employees/", data=patch_data)
        response = self.view(request, emp_no=1008)

        self.assertEqual(response.status_code, status.HTTP_206_PARTIAL_CONTENT)
        self.assertEqual(response.data["firstname"], patch_data["firstname"])
