import factory

from api.models import Productlines


class ProductLinesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Productlines

    productline = factory.sequence(lambda n: n)
