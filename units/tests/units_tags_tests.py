"""Tests for the template tags of the ``units`` app."""
from django.test import TestCase

from ..templatetags import units_tags
from ..utils import convert_value


class ConvertValueTestCase(TestCase):
    """Tests for the ``convert_value`` template tag."""
    longMessage = True

    def test_tag(self):
        self.assertEqual(units_tags.convert_value(10, 'ft'),
                         convert_value(10, 'ft'))
        self.assertEqual(
            units_tags.convert_value(None, 'ft'), '', msg=(
                'When there is no input value, the return value should be'
                ' an empty string.'))
