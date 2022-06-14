from rest_framework import serializers

from api.models import Offices


class OfficesSerializer(serializers.ModelSerializer):
    """
    Serializer class for the offices model
    """
    class Meta:
        model = Offices
        fields = "__all__"

