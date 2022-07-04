import datetime

import factory

from api.models import Orders
from tests.factories.employee_factory import EmployeeFactory


class OrdersFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Orders

    orderdate = datetime.date.today()
    requireddate = datetime.date.today()
    ordernumber = factory.sequence(lambda n: n)
    customernumber = factory.SubFactory(EmployeeFactory)
