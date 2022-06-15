from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Products
from api.products.pagination import ProductPagination
from api.products.serializers import ProductsSerializer


class ProductsListView(APIView):
    """
    View for interacting with the product model without id
    """
    serializer_class = ProductsSerializer
    pagination_class = ProductPagination

    def get(self, request, format=None):
        """
        Retrieve a list of products from the database
        """
        pagination = self.pagination_class()
        products = Products.objects.all()

        results = pagination.paginate_queryset(queryset=products, request=request)
        serializer = self.serializer_class(results, many=True)

        return pagination.get_paginated_response(serializer.data)
