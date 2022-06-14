from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.customers.serializers import CustomerSerializer
from api.models import Customers


class CustomersListView(APIView):
    """
    View for interacting the with customers without id
    """
    serializer_class = CustomerSerializer

    def get(self, request, format=None):
        """
        Retrieve a list of all the customers in the database

        Args:
            request (object) : Request object
            format (str) : Format for rest output e.g json
        Returns:
            Response : Http response
        """
        customers = Customers.objects.all()
        serializer = self.serializer_class(customers, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
