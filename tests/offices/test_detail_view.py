from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory

from api.models import Offices
from api.offices.detail_view import OfficesDetailView
from api.offices.serializers import OfficesSerializer
from tests.factories.office_factory import OfficesFactory


class TestOfficesDetailView(APITestCase):
    """
    Test the offices list view
    """

    def setUp(self) -> None:
        """
        Set up the necessary requirements for the test
        """
        self.factory = APIRequestFactory()
        self.view = OfficesDetailView.as_view()
        self.serializer = OfficesSerializer

    def test_get_by_id(self):
        """
        Test getting an office from the database works fine
        """
        office = OfficesFactory(officecode="OFC-10")

        request = self.factory.get("/api/offices")
        response = self.view(request, office.pk)

        office = Offices.objects.first()
        serializer = self.serializer(instance=office)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["officecode"],
            serializer.data["officecode"]
        )
