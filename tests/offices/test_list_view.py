from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory

from api.models import Offices
from api.offices.list_view import OfficesListView
from tests.factories.office_factory import OfficesFactory


class TestOfficesListView(APITestCase):
    """
    Test the offices list view
    """

    def setUp(self) -> None:
        """
        Set up the necessary requirements for the test
        """
        self.factory = APIRequestFactory()
        self.view = OfficesListView.as_view()

    def test_get(self):
        """
        Test getting offices from the database works fine
        """
        _ = OfficesFactory.create_batch(10)

        request = self.factory.get(reverse("api:offices"))
        response = self.view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Offices.objects.all().count())
