"""Setting defaults for the ``units`` app."""
from django.conf import settings


# NOTE: Overriding these settings is not yet supported. Conversions, queries
# etc will use these setting constans, but not be aware of them being
# different. All units will be calculated as if the standard is used.

# The standard unit for distance and weight, that is stored in the database
DISTANCE_STANDARD_UNIT = getattr(settings, 'DISTANCE_STANDARD_UNIT', 'm')
WEIGHT_STANDARD_UNIT = getattr(settings, 'WEIGHT_STANDARD_UNIT', 'kg')
