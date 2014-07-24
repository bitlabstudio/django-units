"""Utils for the ``units`` app."""
from decimal import Decimal

from django.utils.translation import ugettext_lazy as _

from . import constants, settings as app_settings


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
    if to_unit in constants.DISTANCES.keys():
        distance = True
    elif to_unit in constants.WEIGHTS.keys():
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
        if distance and from_unit not in constants.DISTANCES.keys() or (
                weight and from_unit not in constants.WEIGHTS.keys()):
            raise TypeError(_(
                'Cannot convert between weight and distance types.'))

    if distance:
        normal_factor = constants.DISTANCE_UNITS[from_unit]
        conversion_factor = constants.DISTANCE_UNITS[to_unit]
    else:
        normal_factor = constants.WEIGHT_UNITS[from_unit]
        conversion_factor = constants.WEIGHT_UNITS[to_unit]

    result = ((d(value) * normal_factor) / conversion_factor).normalize()
    sign, digit, exponent = result.as_tuple()
    if exponent <= 0:
        return result
    else:
        return result.quantize(1)
