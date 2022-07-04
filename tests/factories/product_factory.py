import factory
from faker import Faker

from api.models import Products
from tests.factories.productline_factory import ProductLinesFactory

faker = Faker()


class ProductsFactory(factory.django.DjangoModelFactory):
    """
    Factory for creating products objects for testing
    """
    productname = faker.pystr()
    productline = factory.SubFactory(ProductLinesFactory)
    msrp = faker.pydecimal(right_digits=2, positive=True, min_value=2, max_value=100)
    buyprice = faker.pyfloat(positive=True)
    quantityinstock = faker.pyint()
    productcode = factory.sequence(lambda n: f"XX-{n}")

    class Meta:
        model = Products
