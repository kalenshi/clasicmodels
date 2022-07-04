import factory

from api.models import Customers
from tests.factories.employee_factory import EmployeeFactory


class CustomersFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customers

    customernumber = factory.sequence(lambda n: n)
    salesrepemployeenumber = factory.SubFactory(EmployeeFactory)
