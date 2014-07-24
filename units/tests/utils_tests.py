"""Tests for the utils of the ``units`` app."""
from django.test import TestCase

from .. import utils


class ConvertValueTestCase(TestCase):
    """Tests for the ``convert_value`` utility function."""
    longMessage = True

    def test_function(self):
        # convert 1 m to km
        self.assertEqual(utils.convert_value(1, 'km'), utils.d(0.001))

        # convert 1 ft to ft (converts to m and back to ft)
        self.assertEqual(utils.convert_value(1, 'ft', 'ft'), utils.d(1))

        # convert 1 kg to g
        self.assertEqual(utils.convert_value(1, 'g'), utils.d(1000))

        # convert 453.592 g to lbs
        self.assertEqual(utils.convert_value(utils.d(453.592), 'lbs', 'g'),
                         utils.d(1))

        # wrong to unit
        self.assertRaises(TypeError, utils.convert_value, 1, 'foonit')

        # wrong from unit
        self.assertRaises(TypeError, utils.convert_value, 1, 'kg', 'foonit')

        # mismatching from and to unit
        self.assertRaises(TypeError, utils.convert_value, 1, 'kg', 'in')
