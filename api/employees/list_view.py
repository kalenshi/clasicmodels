from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
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

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="employeenumber",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="Employees employeenumber",
                require=False
            ),
            openapi.Parameter(
                name="lastname",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="Employee last name",
                require=False
            ),
            openapi.Parameter(
                name="firstname",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="Employees firstname",
                require=False
            ),
            openapi.Parameter(
                name="extension",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="Employee extension",
                require=False
            ),
            openapi.Parameter(
                name="email",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="Employees email",
                require=False
            ),
            openapi.Parameter(
                name="officecode",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Employee officecode",
                require=False
            ),
            openapi.Parameter(
                name="reportsto",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Employee supervisor",
                require=False
            ),
        ]
    )
    def get(self, request, format=None):
        """
        Retrieve a list of all the customers in the database

        Args:
            request (object) : Request object
            format (str) : Format for rest output e.g json
        Returns:
            Response : Http response
        """

        # Gather the filters
        filters = {
            "employeenumber": request.GET.get("employeenumber"),
            "lastname": request.GET.get("lastname"),
            "firstname": request.GET.get("firstname"),
            "extension": request.GET.get("extension"),
            "email": request.GET.get("email"),
            "officecode": request.GET.get("officecode"),
            "reportsto": request.GET.get("reportsto")
        }

        # Drop none values in filters
        filters = {k: v for k, v in filters.items() if v is not None}

        paginator = self.pagination_class()
        employees = Employees.objects.select_related(
            "officecode", "reportsto"
        ).filter(**filters).order_by("employeenumber")

        result = paginator.paginate_queryset(employees, request)

        serializer = self.serializer_class(result, many=True)

        return paginator.get_paginated_response(data=serializer.data)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "firstname": openapi.Schema(type=openapi.TYPE_STRING),
                "lastname": openapi.Schema(type=openapi.TYPE_STRING),
                "extension": openapi.Schema(type=openapi.TYPE_STRING),
                "email": openapi.Schema(type=openapi.TYPE_STRING),
                "officecode": openapi.Schema(type=openapi.TYPE_INTEGER),
                "reportsto": openapi.Schema(type=openapi.TYPE_INTEGER),
            },
            required=["firstname", "lastname", "extension", "email", "officecode", "reportsto"]
        )

    )
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
