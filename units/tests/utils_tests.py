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

        # convert g to kg without to_unit
        self.assertEqual(utils.convert_value(1000, from_unit='g'), utils.d(1))

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

        # no units given
        self.assertRaises(TypeError, utils.convert_value, 1)


class CleanFeetInchTestCase(TestCase):
    """Tests for the ``clean_feet_inch`` utility funcion."""
    longMessage = True

    def test_function(self):
        # decimals are passed right through
        self.assertEqual(utils.clean_feet_inch(utils.d(1.1)), utils.d(1.1))

        # floats or ints are passed through as decimal
        self.assertEqual(utils.clean_feet_inch(1.1), utils.d(1.1))

        # strings are normalized to decimal
        self.assertEqual(utils.clean_feet_inch('2\'3"'), utils.d(2.25))

        # strings omitting the inches are normalized to decimal
        self.assertEqual(utils.clean_feet_inch('2\''), utils.d(2))

        # strings omitting the feet value are normalized to decimal
        self.assertEqual(utils.clean_feet_inch('3"'), utils.d(0.25))
