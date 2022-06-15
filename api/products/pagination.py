from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination


class ProductPagination(LimitOffsetPagination):
    """
    Pagination class for the products returned from the database
    """
    limit_query_param = "limit"
    offset_query_param = "offset"
    limit = 1
    offset = 0

    def get_paginated_response(self, data):
        """
        Overriding the base get_paginated_response to change the count variable to total
        Args:
            data (dict) : data to paginate
        Returns:
            Response : An http Response object
        """
        return Response({
            "links": {
                "next": self.get_next_link(),
                "previous": self.get_previous_link()
            },
            "total": self.count,
            "results": data
        })
