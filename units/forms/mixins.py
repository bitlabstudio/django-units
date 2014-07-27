"""Form mixins to handle unit model fields better."""
from django.forms import ValidationError

from .. import utils

# TODO initialize with correct format and unit


class UnitsFormMixin(object):
    """
    Mixin to handle custom validation, cleaning and pre-save operations
    on ModelForms for models with value/unit pair fields.

    Required attribute ``value_fieldsets`` ties together the value and unit
    fields of the model, so that the form knows what to validate together
    automatically. Example:::

        value_fieldsets = [
            ('distance', 'distance_unit'),
            ('weight', 'weight_unit'),
        ]

    """

    def clean_fieldset_method(self, value_field, unit_field):
        def clean_method():
            value = self.data.get(value_field)
            unit = self.data.get(unit_field)
            # convert it to standard unit
            try:
                cleaned_value = utils.convert_value(value, from_unit=unit)
            except TypeError as ex:
                raise ValidationError(ex)
            return cleaned_value
        return clean_method

    def __init__(self, *args, **kwargs):
        for fieldset in getattr(self, 'value_fieldsets', []):
            setattr(
                self,
                'clean_{0}'.format(fieldset[0]),
                self.clean_fieldset_method(fieldset[0], fieldset[1]),
            )
        super(UnitsFormMixin, self).__init__(*args, **kwargs)
