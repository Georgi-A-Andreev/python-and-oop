import re

from django.core.exceptions import ValidationError


def validate_name(value):
    for c in value:
        if not (c.isalpha() or c.isspace()):
            raise ValidationError('Name can only contain letters and spaces')


def validate_phone_number(value):
    if not re.match(r'^\+359\d{9}$', value):
        raise ValidationError("Phone number must start with a '+359' followed by 9 digits")
