from rest_framework.test import APITestCase

from tests.factories.office_factory import OfficesFactory


class TestOfficesModel(APITestCase):
    """
    Test the offices model's string function
    """

    def setUp(self) -> None:
        """
        Create an offices instance
        """
        self.office = OfficesFactory(officecode="XX")

    def test_string_representation(self):
        self.assertEqual(self.office.__str__(), "Office-XX")
