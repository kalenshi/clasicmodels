from rest_framework.test import APITestCase

from tests.factories.employee_factory import EmployeeFactory


class TestEmployeesModel(APITestCase):
    """
    Test the employee model's string function
    """

    def setUp(self) -> None:
        """
        Create an employee instance
        """
        self.customer = EmployeeFactory(employeenumber=1003)

    def test_string_representation(self):
        self.assertEqual(self.customer.__str__(), "Employee-1003")
