from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.employees.serializers import EmployeeSerializer
from api.models import Employees


class SupervisorsListView(APIView):
    """
    View for interacting the with supervisors without id
    """
    serializer_class = EmployeeSerializer

    def get(self, request, format=None):
        """
        Retrieve a list of all the Employees who are supervisors in the database

        Args:
            request (object) : Request object
            format (str) : Format for rest output e.g json
        Returns:
            Response : Http response
        """
        supervisor_list = Employees.objects.values_list("reportsto", flat=True).distinct()
        supervisors = Employees.objects.filter(
            Q(employeenumber__in=supervisor_list) |
            Q(reportsto=None)
        )

        serializer = self.serializer_class(supervisors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
