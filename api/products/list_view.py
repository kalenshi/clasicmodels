from drf_yasg import openapi
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from api.models import Products
from api.products.pagination import ProductPagination
from api.products.serializers import ProductsSerializer


class ProductsListView(APIView):
    """
    View for interacting with the product model without id
    based on the provided filters
    """
    serializer_class = ProductsSerializer
    pagination_class = ProductPagination

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="productcode",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="Product code",
                require=False
            ),
            openapi.Parameter(
                name="productname",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="Product code",
                require=False
            ),
        ]
    )
    def get(self, request, format=None):
        """
        Retrieve a list of products from the database
        """
        pagination = self.pagination_class()
        products = Products.objects.all()

        results = pagination.paginate_queryset(queryset=products, request=request)
        serializer = self.serializer_class(results, many=True)

        return pagination.get_paginated_response(serializer.data)
