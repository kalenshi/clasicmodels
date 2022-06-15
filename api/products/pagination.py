from rest_framework.pagination import PageNumberPagination


class ProductPagination(PageNumberPagination):
    """
    Pagination class for the products returned from the database
    """
    page_size = 10
    page_query_param = "page"
    page_size_query_param = "page_size"
    max_page_size = 50
