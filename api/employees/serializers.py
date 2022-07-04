from rest_framework import serializers

from api.models import Employees, Offices


class EmployeeSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Employees model
    """
    officecode = serializers.PrimaryKeyRelatedField(queryset=Offices.objects.all())
    reportsto = serializers.PrimaryKeyRelatedField(queryset=Employees.objects.all())

    class Meta:
        model = Employees
        fields = (
            "employeenumber",
            "lastname",
            "firstname",
            "extension",
            "email",
            "officecode",
            "reportsto",
            "jobtitle",
            "manages",
            "active",
        )
        read_only_fields = ("employeenumber", "manages")
