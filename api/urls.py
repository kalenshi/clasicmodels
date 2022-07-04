from django.urls import path

from api.customers.detail_view import CustomersDetailView
from api.customers.list_view import CustomersListView
from api.employees.detail_view import EmployeesDetailView
from api.employees.list_view import EmployeesListView
from api.offices.detail_view import OfficesDetailView
from api.offices.list_view import OfficesListView
from api.products.detail_view import ProductsDetailView
from api.products.list_view import ProductsListView
from api.supervisor.detail_view import SupervisorsDetailView
from api.supervisor.list_view import SupervisorsListView

app_name = "api"

urlpatterns = [
    path("customers/", CustomersListView.as_view(), name="customers"),
    path("customers/<cust_id>", CustomersDetailView.as_view(), name="customer_detail"),
    path("employees/", EmployeesListView.as_view(), name="employees"),
    path("employees/<emp_no>", EmployeesDetailView.as_view(), name="employee_detail"),
    path("supervisors/", SupervisorsListView.as_view(), name="supervisors"),
    path("supervisors/<emp_no>", SupervisorsDetailView.as_view(), name="supervisor_detail"),
    path("offices/", OfficesListView.as_view(), name="offices"),
    path("offices/<officecode>", OfficesDetailView.as_view(), name="office_detail"),
    path("products/", ProductsListView.as_view(), name="products"),
    path("products/<productno>", ProductsDetailView.as_view(), name="products_detail"),
]
