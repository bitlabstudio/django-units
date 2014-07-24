"""Global constants for the ``units`` app."""
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
    'cm': 0.01,
    'ft': 0.3048,
    'in': 0.0254,
    'km': 1000.0,
    'm': 1.0,
    'mi': 1609.344,
    'mm': 0.001,
}

DISTANCE_DEFAULT_CHOICES = {
    'cm': DISTANCES['cm'],
    'ft': DISTANCES['ft'],
    'in': DISTANCES['in'],
    'km': DISTANCES['km'],
    'm': DISTANCES['m'],
    'mi': DISTANCES['mi'],
    'mm': DISTANCES['mm'],
}

WEIGHTS = {
    'g': _('gram'),
    'kg': _('kilogram'),
    'lbs': _('pound'),
    'oz': _('ounce'),
}

WEIGHT_UNITS = {
    'g': 0.001,
    'kg': 1.0,
    'lbs': 0.453592,
    'oz': 0.0283495,
}

WEIGHT_DEFAULT_CHOICES = (
    ('g', WEIGHTS['g']),
    ('kg', WEIGHTS['kg']),
    ('lbs', WEIGHTS['lbs']),
    ('oz', WEIGHTS['oz']),
)
