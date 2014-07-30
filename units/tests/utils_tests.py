"""Tests for the utils of the ``units`` app."""
from django.test import TestCase

from .. import utils


class CleanFeetInchTestCase(TestCase):
    """Tests for the ``clean_feet_inch`` utility funcion."""
    longMessage = True

    def test_function(self):
        # decimals are passed right through
        self.assertEqual(utils.clean_feet_inch(utils.d(1.1)), utils.d(1.1))

        # floats or ints are passed through as decimal
        self.assertEqual(utils.clean_feet_inch(1.1), utils.d(1.1))

        # strings in float format are converted to decimal
        self.assertEqual(utils.clean_feet_inch('1.1'), utils.d(1.1))

        # strings are normalized to decimal
        self.assertEqual(utils.clean_feet_inch('2\'3"'), utils.d(2.25))

        # strings omitting the inches are normalized to decimal
        self.assertEqual(utils.clean_feet_inch('2\''), utils.d(2))

        # strings omitting the feet value are normalized to decimal
        self.assertEqual(utils.clean_feet_inch('3"'), utils.d(0.25))


class ToFeetTestCase(TestCase):
    """Tests for the ``to_feet`` utility function."""
    longMessage = True

    def test_function(self):
        self.assertEqual(utils.to_feet(utils.d(1.5)), '1\'6"')
        self.assertEqual(utils.to_feet(utils.d(2)), '2\'')
        self.assertEqual(utils.to_feet(utils.d(0.5)), '6"')


class ConvertValueTestCase(TestCase):
    """Tests for the ``convert_value`` utility function."""
    longMessage = True

    def test_function(self):
        # convert 1 m to km
        self.assertEqual(utils.convert_value(1, 'km'), utils.d(0.001))

        # convert ft to ft with alternate notation
        self.assertEqual(utils.convert_value("1'6\"", 'ft', 'ft'), "1'6\"")

        # convert 1 ft to ft (converts to m and back to ft)
        self.assertEqual(utils.convert_value(1, 'ft', 'ft'), '1\'')

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

        # regression tests
        lbs = 160
        kg = utils.convert_value(160, from_unit='lbs')
        self.assertEqual(utils.convert_value(kg, to_unit='lbs'), lbs, msg=(
            'When converting from lbs into kg and back, the value should be'
            ' the same again.'))
