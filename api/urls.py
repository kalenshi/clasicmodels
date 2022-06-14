from django.urls import path

from api.customers.detail_view import CustomersDetailView
from api.customers.list_view import CustomersListView
from api.employees.detail_view import EmployeesDetailView
from api.employees.list_view import EmployeesListView
from api.offices.detail_view import OfficesDetailView
from api.offices.list_view import OfficesListView
from api.supervisor.list_view import SupervisorsListView

urlpatterns = [
    path("customers/", CustomersListView.as_view(), name="customers"),
    path("customers/<cust_id>", CustomersDetailView.as_view(), name="customer_detail"),
    path("employees/", EmployeesListView.as_view(), name="employees"),
    path("employees/<emp_no>", EmployeesDetailView.as_view(), name="employee_detail"),
    path("supervisors/", SupervisorsListView.as_view(), name="supervisors"),
    path("supervisors/<emp_no>", EmployeesDetailView.as_view(), name="employee_detail"),
    path("offices/", OfficesListView.as_view(), name="offices"),
    path("offices/<officecode>", OfficesDetailView.as_view(), name="office_detail"),
]
