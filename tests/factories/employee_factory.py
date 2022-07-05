import factory
from faker import Faker

from api.models import Employees
from tests.factories.office_factory import OfficesFactory

faker = Faker()

titles = [
    "VP Sales",
    "VP Marketing",
    "Sales Manager (APAC)",
    "Sale Manager (EMEA)",
    "Sales Manager (NA)"
]


class EmployeeFactory(factory.django.DjangoModelFactory):
    """
    Factory for creating employee models for testing
    """

    employeenumber = factory.sequence(lambda n: n)
    officecode = factory.SubFactory(OfficesFactory)
    jobtitle = faker.random_element(elements=titles)

    class Meta:
        model = Employees
