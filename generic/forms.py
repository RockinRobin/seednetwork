# -*- coding: utf-8 -*-
"""generic(english) specific Form helpers."""

from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError
from django.forms.fields import Field, Select
from django.utils.translation import ugettext_lazy

class CountryField(Field):
    """
    A form field that validates its input is a Country (english) name or abbreviation.
    It normalizes the input to the standard two-leter iso 3166 code
    abbreviation for the given country.
    Note, the normalization is poor and does not 'clean' the countries well.
    Given the unicode characters, long country names etc this could be an arduous task to fix.
    Intended use is currently with  the widget.
    """

    default_error_messages = {
        'invalid': ugettext_lazy('Enter a Country.'),
    }

    def clean(self, value):
        from .iso_3166_english import COUNTRY_MAP_ENGLISH
        country_dict_inverse = {c[1]:c[0] for c in COUNTRY_MAP_ENGLISH}
        country_dict_self = {c[0]:c[0] for c in COUNTRY_MAP_ENGLISH}
        country_dict = merge_two_dicts(country_dict_self, country_dict_inverse)
        super(CountryField, self).clean(value)
        if value in EMPTY_VALUES:
            return ''
        try:
            value = value.strip()
        except AttributeError:
            pass
        else:
            try:
                return country_dict[value.strip()]
            except KeyError:
                pass
        raise ValidationError(self.error_messages['invalid'])


class CountrySelect(Select):
    """A Select widget that uses a list of Counties (english)  as its choices."""

    def __init__(self, attrs=None):
        from .iso_3166_english  import COUNTRY_MAP_ENGLISH
        super(CountrySelect, self).__init__(attrs, choices=COUNTRY_MAP_ENGLISH)

def merge_two_dicts(x, y):
    """Given two dicts, merge them into a new dict as a shallow copy."""
    z = x.copy()
    z.update(y)
    return z
