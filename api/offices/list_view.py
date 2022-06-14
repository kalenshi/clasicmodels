from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Offices
from api.offices.serializers import OfficesSerializer


class OfficesListView(APIView):
    """
    class for interacting the office model without id
    """
    serializer_class = OfficesSerializer

    def get(self, request, format=None):
        """
        Retrieve a list of offices from the database
        """
        offices = Offices.objects.all()
        serializer = self.serializer_class(offices, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
