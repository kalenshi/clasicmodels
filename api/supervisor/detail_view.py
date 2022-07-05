from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.employees.serializers import EmployeeSerializer
from api.models import Employees


class SupervisorsDetailView(APIView):
    """
    View for interacting the with a specific supervisors by id
    """
    serializer_class = EmployeeSerializer

    def get_object(self, pk):
        """
        Retrieve a specif employee with all the employees it supervises
        Args:
            pk (int) : the primary key of the employee
        Returns:
            Employees : an employee object with its subordinates

        """
        try:
            return Employees.objects.prefetch_related("manages").get(pk=pk)
        except ObjectDoesNotExist:
            raise Exception(f"Employee with employeenumber {pk} Does not exist!")

    def get(self, request, emp_no, format=None):
        """
        Retrieve a specific Employees with a list of subordinates

        Args:
            request (object) : Request object
            format (str) : Format for rest output e.g json
        Returns:
            Response : Http response
        """
        employee = self.get_object(emp_no)

        serializer = self.serializer_class(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
