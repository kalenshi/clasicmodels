from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.employees.pagination import EmployeePagination
from api.employees.serializers import EmployeeSerializer
from api.models import Employees


class EmployeesListView(APIView):
    """
    View for interacting the with employees without id
    """
    serializer_class = EmployeeSerializer
    pagination_class = EmployeePagination

    def get(self, request, format=None):
        """
        Retrieve a list of all the customers in the database

        Args:
            request (object) : Request object
            format (str) : Format for rest output e.g json
        Returns:
            Response : Http response
        """

        paginator = self.pagination_class()
        employees = Employees.objects.select_related("officecode", "reportsto").all()
        result = paginator.paginate_queryset(employees, request)

        serializer = self.serializer_class(result, many=True)

        return paginator.get_paginated_response(data=serializer.data)

    def post(self, request, format=None):
        """
        Creates a new Employee in the database and returns it
        Args:
            request (object) : Request object
            format (str) : Format for rest output e.g json
        Returns:
            Response : Http response

        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
