"""Test models."""
from django.db import models
from django.utils.translation import ugettext_lazy as _

from units import constants


class Dummymodel(models.Model):
    distance = models.DecimalField(
        verbose_name=_('Distance'),
        max_digits=15,
        decimal_places=4,
        blank=True, null=True,
    )

    distance_unit = models.CharField(
        verbose_name=_('Distance unit'),
        max_length=64,
        choices=constants.DISTANCE_DEFAULT_CHOICES,
        blank=True,
    )

    weight = models.DecimalField(
        verbose_name=_('Weight'),
        max_digits=15,
        decimal_places=4,
        blank=True, null=True,
    )

    weight_unit = models.CharField(
        verbose_name=_('Weight unit'),
        max_length=64,
        choices=constants.WEIGHT_DEFAULT_CHOICES,
        blank=True,
    )

    # just some additional other fields, to be sure our mixin does not mess
    # with them or break any regular form functionality

    another_value = models.DecimalField(
        verbose_name=_('Another value'),
        max_digits=15,
        decimal_places=4,
        blank=True, null=True,
    )

    another_char = models.CharField(
        verbose_name=_('Another char'),
        max_length=64,
        blank=True,
    )
