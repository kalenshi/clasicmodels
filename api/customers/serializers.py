from rest_framework import serializers

from api.models import Customers


class CustomerSerializer(serializers.ModelSerializer):
    """
    Serializers class for the customers model
    """

    class Meta:
        model = Customers
        fields = "__all__"
        read_only_fields = ("employeenumber", "customernumber")
