from rest_framework import serializers

from api.models import Employees


class EmployeeSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Employees model
    """
    officecode = serializers.SlugRelatedField(slug_field="postalcode", read_only=True)
    reportsto = serializers.SlugRelatedField(slug_field="jobtitle", read_only=True)
    manages = serializers.SlugRelatedField(many=True, read_only=True, slug_field="firstname")

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
