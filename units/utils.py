"""Utils for the ``units`` app."""
import re

from decimal import Decimal

from django.utils.translation import ugettext_lazy as _

from . import (
    constants as const,
    settings as app_settings,
)


def d(val):
    """A shortcut for decimal conversion."""
    # a float needs to be converted to a string before passing it into Decimal
    # otherwise it'll be stored with major roundig errors
    return Decimal(str(val))


def convert_value(value, to_unit, from_unit=None):
    """
    Outputs the value as decimal in the unit specified.

    :param value: The value as decimal, float or int, that needs to be
      converted.
    :param to_unit: A string with the short version of the unit, that should
      be converted into. E.g. 'm'.
    :param from_unit: A string with the short version of the unit, that the
        value is in. E.g. 'ft'. If it's left empty, the default is used.

    """
    distance = False
    normal_factor = d(1.0)
    conversion_factor = d(1.0)
    weight = False

    # check if, we're calculating weights or distances
    if to_unit in const.DISTANCES.keys():
        distance = True
    elif to_unit in const.WEIGHTS.keys():
        weight = True
    else:
        raise TypeError(_('The unit is not one of the allowed types.'))

    # get the standard from_unit if it's not defined
    if from_unit is None:
        if distance:
            from_unit = app_settings.DISTANCE_STANDARD_UNIT
        else:
            from_unit = app_settings.WEIGHT_STANDARD_UNIT
    else:
        if distance and from_unit not in const.DISTANCES.keys() or (
                weight and from_unit not in const.WEIGHTS.keys()):
            raise TypeError(_(
                'Cannot convert between weight and distance types.'))

    if distance:
        normal_factor = const.DISTANCE_UNITS[from_unit]
        conversion_factor = const.DISTANCE_UNITS[to_unit]
    else:
        normal_factor = const.WEIGHT_UNITS[from_unit]
        conversion_factor = const.WEIGHT_UNITS[to_unit]

    result = ((d(value) * normal_factor) / conversion_factor).normalize()
    sign, digit, exponent = result.as_tuple()
    if exponent <= 0:
        return result
    else:
        return result.quantize(1)


def clean_feet_inch(value):
    """
    Normalizes x'y" format for feet and inch to a feet decimal.

    e.g. 1'6" becomes 1.5

    """
    pattern = re.compile("(?P<foot>\d+)'\s?(?P<inch>\d+)\"")

    # if we happen to have a numerical type already we can just output it
    if isinstance(value, Decimal):
        return value

    if isinstance(value, float) or isinstance(value, int):
        return d(value)

    feet, inch = re.match(pattern, value).groups()

    conversion_factor = const.DISTANCE_UNITS['ft'] / const.DISTANCE_UNITS['in']

    result = d(feet) + d(inch) / d(conversion_factor)

    return result
