"""Factories for models and dummy models of the ``units`` app."""
from decimal import Decimal

import factory

from units.tests.test_app import models as test_models


class DummymodelFactory(factory.DjangoModelFactory):
    """Factory for the ``Dummymodel`` model."""
    FACTORY_FOR = test_models.Dummymodel

    distance = Decimal('1.2')
    distance_unit = factory.Sequence(lambda n: u'distance_unit {0}'.format(n))
    weight = Decimal('2.4')
    weight_unit = factory.Sequence(lambda n: u'weight_unit {0}'.format(n))
    another_value = Decimal('0.1')
    another_char = factory.Sequence(lambda n: u'another_char {0}'.format(n))
