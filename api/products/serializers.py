from rest_framework import serializers

from api.models import Products


class ProductsSerializer(serializers.ModelSerializer):
    """
    Serializer class for the product model
    """

    class Meta:
        model = Products
        fields = "__all__"
