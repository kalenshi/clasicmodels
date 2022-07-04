import factory

from api.models import Offices


class OfficesFactory(factory.django.DjangoModelFactory):
    """
    Factory for creating offices objects for testing
    """
    officecode = factory.sequence(lambda n: n)

    class Meta:
        model = Offices
