"""Template tags for the ``units`` app."""
from django import template

from ..utils import convert_value as convert_value_util


register = template.Library()


@register.simple_tag()
def convert_value(value, to_unit, from_unit=None):
    """Calls ``convert_value`` inside a template."""
    if not value:
        return ''
    return convert_value_util(value, to_unit, from_unit)
