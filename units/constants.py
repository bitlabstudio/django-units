"""Global constants for the ``units`` app."""
from decimal import Decimal

from django.utils.translation import ugettext_lazy as _

DISTANCES = {
    'cm': _('centimetre'),
    'ft': _('foot'),
    'in': _('inch'),
    'km': _('kilometre'),
    'm': _('metre'),
    'mi': _('mile'),
    'mm': _('millimetre'),
}

DISTANCE_UNITS = {
    'cm': Decimal('0.01'),
    'ft': Decimal('0.3048'),
    'in': Decimal('0.0254'),
    'km': Decimal('1000.0'),
    'm': Decimal('1.0'),
    'mi': Decimal('1609.344'),
    'mm': Decimal('0.001'),
}

DISTANCE_DEFAULT_CHOICES = (
    ('cm', DISTANCES['cm']),
    ('ft', DISTANCES['ft']),
    ('in', DISTANCES['in']),
    ('km', DISTANCES['km']),
    ('m', DISTANCES['m']),
    ('mi', DISTANCES['mi']),
    ('mm', DISTANCES['mm']),
)

WEIGHTS = {
    'g': _('gram'),
    'kg': _('kilogram'),
    'lbs': _('pound'),
    'oz': _('ounce'),
}

WEIGHT_UNITS = {
    'g': Decimal('0.001'),
    'kg': Decimal('1.0'),
    'lbs': Decimal('0.453592'),
    'oz': Decimal('0.0283495'),
}

WEIGHT_DEFAULT_CHOICES = (
    ('g', WEIGHTS['g']),
    ('kg', WEIGHTS['kg']),
    ('lbs', WEIGHTS['lbs']),
    ('oz', WEIGHTS['oz']),
)
