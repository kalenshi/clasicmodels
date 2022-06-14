from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.employees.serializers import EmployeeSerializer
from api.models import Employees


class EmployeesDetailView(APIView):
    """
    View for interacting the with  specific Employee by id
    """
    serializer_class = EmployeeSerializer

    def get_object(self, pk):
        """
        Retrieve a specific object from the database by its primary key
        """
        return get_object_or_404(Employees, pk=pk)

    def get(self, request, emp_no, format=None):
        """
        Retrieve an employee in the database

        Args:
            request (object) : Request object
            emp_no (int) : Employees' primary key value
            format (str) : Format for rest output e.g. json
        Returns:
            Response : Http response
        """
        employee = self.get_object(emp_no)
        serializer = self.serializer_class(employee)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, emp_no, format=None):
        """
        Deletes an existing employee by setting active to false
        Args:
            request (object): request object
            emp_no (int) : Employee number object
            format (str) :  Format for rest output e.g. json
        Returns:
            Response: Http Response
        """
        employee = self.get_object(emp_no)
        employee.active = False
        employee.save()

        serializer = self.serializer_class(instance=employee)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, emp_no, format=None):
        """
        Facilitates partial updates of an existing Employee

           Args:
            request (object): request object
            emp_no (int) : Employee number object
            format (str) :  Format for rest output e.g. json

        Returns:
            Response: Http Response
        """
        employee = self.get_object(emp_no)
        serializer = self.serializer_class(instance=employee, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)
