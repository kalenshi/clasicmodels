from rest_framework.pagination import PageNumberPagination


class EmployeePagination(PageNumberPagination):
    """
    Reduce the number of employees returned by returning a paginated response
    """
    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 100
