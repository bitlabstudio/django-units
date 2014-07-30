"""Utils for the ``units`` app."""
import re
from decimal import Decimal

from django.utils import six

from . import (
    constants as const,
    exceptions,
    settings as app_settings,
)


def d(val):
    """A shortcut for decimal conversion."""
    # a float needs to be converted to a string before passing it into Decimal
    # otherwise it'll be stored with major roundig errors
    return Decimal(str(val))


def clean_feet_inch(value):
    """
    Normalizes x'y" format for feet and inch to a feet decimal.

    e.g. 1'6" becomes 1.5

    """
    pattern = re.compile("(?P<foot>\d+)?'?\s?(?P<inch>\d+)?\"?")

    # if we happen to have a numerical type already we can just output it
    if isinstance(value, Decimal):
        return value

    if isinstance(value, float) or isinstance(value, int):
        return d(value)

    if isinstance(value, six.string_types) and \
            '"' not in value and "'" not in value:
        return d(value)

    feet, inch = re.match(pattern, value).groups()

    if inch is not None:
        conversion_factor = const.DISTANCE_UNITS['ft'] / const.DISTANCE_UNITS['in']
        result = d(feet) + d(inch) / d(conversion_factor)
        return result
    elif "'" in value:
        # if there's only one value and there's a single quotation mark, we
        # know that the value must be in feet
        return d(feet)
    elif '"' in value:
        # if there's only one value and there's a double quotation mark, we
        # know that the value must be in inch. The value from the tuple is
        # still called "feet" though, so don't be mislead by this
        conversion_factor = const.DISTANCE_UNITS['ft'] / const.DISTANCE_UNITS['in']
        return d(feet) / d(conversion_factor)


def to_feet(value):
    """Converts a decimal to a feet/inch notation string."""
    inches = ''
    feet = ''
    rounded = d(int(value))
    rest = value - rounded
    rest_in = rest * d(12)
    if rest_in:
        inches = '{0}"'.format(int(round(rest_in)))
    if rounded:
        feet = "{0}'".format(rounded)
    return feet + inches


def convert_value(value, to_unit=None, from_unit=None):
    """
    Outputs the value as decimal in the unit specified.

    :param value: The value as decimal, float or int, that needs to be
      converted.
    :param to_unit: A string with the short version of the unit, that should
      be converted into. E.g. 'm'. If it's left empty, the default is used.
    :param from_unit: A string with the short version of the unit, that the
        value is in. E.g. 'ft'. If it's left empty, the default is used.

    Note, that either ``from_unit`` or ``to_unit`` must be given.

    """
    conversion_dict = {}
    conversion_factor = d(1.0)
    default_unit = None
    found_unit = None
    normal_factor = d(1.0)

    # either of the units must be given
    if from_unit is None and to_unit is None:
        raise TypeError('Either ``to_unit`` or ``from_unit`` must be defined.')

    # check if, we're calculating weights or distances
    if to_unit is not None:
        found_unit = to_unit
    elif from_unit is not None:
        found_unit = from_unit

    if found_unit in const.DISTANCES.keys():
        conversion_dict = const.DISTANCE_UNITS
        default_unit = app_settings.DISTANCE_STANDARD_UNIT
    elif found_unit in const.WEIGHTS.keys():
        conversion_dict = const.WEIGHT_UNITS
        default_unit = app_settings.WEIGHT_STANDARD_UNIT
    else:
        raise exceptions.WrongUnitError(
            '{0} is not one of the allowed units.'.format(found_unit))

    # get the standard from_unit if it's not defined
    if from_unit is None:
        from_unit = default_unit
    elif to_unit is None:
        to_unit = default_unit

    if from_unit not in conversion_dict or to_unit not in conversion_dict:
        raise TypeError(
            'Cannot convert between ``{0}`` and ``{1}``.'.format(
                from_unit, to_unit))

    normal_factor = conversion_dict[from_unit]
    conversion_factor = conversion_dict[to_unit]

    # check if the value needst to be converted from the feet/inch form into
    # decimal
    if isinstance(value, six.string_types) and (
            '"' in value or "'" in value):
        value = clean_feet_inch(value)

    result = ((d(value) * normal_factor) / conversion_factor).normalize()
    if to_unit == 'ft':
        return to_feet(result)

    sign, digit, exponent = result.as_tuple()
    if exponent <= 0:
        return result
    else:
        return result.quantize(1)
