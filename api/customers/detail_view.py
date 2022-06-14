from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.customers.serializers import CustomerSerializer
from api.models import Customers


class CustomersDetailView(APIView):
    """
    View for interacting the with  specific customers by id
    """
    serializer_class = CustomerSerializer

    def get_object(self, pk):
        """
        Retrieve a specific object from the database by its primary key
        """
        return get_object_or_404(Customers, pk=pk)

    def get(self, request, cust_id, format=None):
        """
        Retrieve a customer in the database

        Args:
            request (object) : Request object
            cust_id (int) : Customers' primary key value
            format (str) : Format for rest output e.g json
        Returns:
            Response : Http response
        """
        customer = self.get_object(cust_id)
        serializer = self.serializer_class(customer)

        return Response(serializer.data, status=status.HTTP_200_OK)
