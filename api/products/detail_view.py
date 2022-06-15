from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Products
from api.products.serializers import ProductsSerializer


class ProductsDetailView(APIView):
    """
    View for interacting with the product model with an  id
    """
    serializer_class = ProductsSerializer

    def get_object(self, pk):
        """
        Retrieve a single product object from the database

        Args:
            pk (int) : the primary ke of the product
        Returns:
            object : Product model with the specified key
        """
        return get_object_or_404(Products, pk=pk)

    def get(self, request, productno, format=None):
        """
        Retrieve a list of products from the database
        """
        product = self.get_object(productno)
        serializer = self.serializer_class(product)

        return Response(serializer.data, status=status.HTTP_200_OK)
