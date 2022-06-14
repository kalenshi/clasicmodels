from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from api.models import Offices
from api.offices.serializers import OfficesSerializer


class OfficesDetailView(APIView):
    """
    View for interacting with the office model by id
    """
    serializer_class = OfficesSerializer

    def get_object(self, pk):
        """
        Retrieve a specific office by id

        Args:
            pk (int) : the primary key of the specific office
        Returns:
            object : The retrieved Offices object if no exception is raised
        """

        return get_object_or_404(Offices, pk=pk)

    def get(self, request, officecode, format=None):
        """
        Get the details of an office by it's id
        Args:
            officecode (int) : The offices' primary key
        Returns:
            Response : an HTTP response object
        """
        office_obj = self.get_object(officecode)

        # get all employees at this office
        employees = office_obj.office.all().values("firstname", "lastname", "employeenumber")
        serializer = self.serializer_class(instance=office_obj)

        response = {**serializer.data}
        response.update({"employees": [*employees]})

        return Response(response, status=status.HTTP_200_OK)
