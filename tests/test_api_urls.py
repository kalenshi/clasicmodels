from django.test import SimpleTestCase
from django.urls import reverse, resolve
from rest_framework.test import APITestCase

from api.employees.list_view import EmployeesListView


class TestAPIUrlsResolve(APITestCase):
    """
    Tests that the urls resolve correctly to the right views
    """

    def test_get_employees_resolve(self):
        """
        Test the employees endpoint resolves to the correct view
        """
        url = reverse("api:employees")
        self.assertEqual(resolve(url).func.view_class, EmployeesListView)
