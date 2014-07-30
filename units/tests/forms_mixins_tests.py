"""Tests for the form mixins of the ``units`` app."""
from decimal import Decimal

from django import forms
from django.test import TestCase

from .test_app.models import Dummymodel
from ..forms import mixins


class DummymodelForm(mixins.UnitsFormMixin, forms.ModelForm):
    value_fieldsets = [
        ('distance', 'distance_unit'),
        ('weight', 'weight_unit'),
    ]

    class Meta:
        model = Dummymodel


class UnitsFormMixinTestCase(TestCase):
    longMessage = True

    def setUp(self):
        self.data = {
            'another_char': 'test',
            'another_value': Decimal('1.4'),
            'distance': Decimal('250'),
            'distance_unit': 'cm',
            'weight': Decimal('160'),
            'weight_unit': 'lbs',
        }

    def test_form(self):
        form = DummymodelForm(data=self.data)
        self.assertTrue(form.is_valid(), msg=(
            'The form should be valid. Errors: {0}'.format(form.errors)))

        obj = form.save()

        self.assertEqual(obj.distance, Decimal('2.5'))
        self.assertEqual(obj.distance_unit, 'cm')
        self.assertEqual(obj.weight, Decimal('72.57472'))
        self.assertEqual(obj.weight_unit, 'lbs')

        form = DummymodelForm(instance=obj)
        self.assertEqual(form.initial['distance'], self.data['distance'])
        self.assertEqual(form.initial['weight'], self.data['weight'])

        bad_data = self.data.copy()
        bad_data.update({'weight_unit': 'furlong'})
        form = DummymodelForm(data=bad_data)
        self.assertFalse(form.is_valid(), msg='The form should not be valid.')

        bad_data = self.data.copy()
        bad_data.pop('weight_unit')
        form = DummymodelForm(data=bad_data)
        self.assertFalse(form.is_valid(), msg='The form should not be valid.')
