from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.customers.pagination import CustomerPagination
from api.customers.serializers import CustomerSerializer
from api.models import Customers


class CustomersListView(APIView):
    """
    View for interacting the with customers without id
    """
    serializer_class = CustomerSerializer
    pagination_class = CustomerPagination

    def get(self, request, format=None):
        """
        Retrieve a list of all the customers in the database

        Args:
            request (object) : Request object
            format (str) : Format for rest output e.g json
        Returns:
            Response : Http response
        """
        pagination = self.pagination_class()
        queryset = Customers.objects.all().order_by("customernumber")
        customers = pagination.paginate_queryset(queryset, request)
        serializer = self.serializer_class(customers, many=True)

        return pagination.get_paginated_response(data=serializer.data)
