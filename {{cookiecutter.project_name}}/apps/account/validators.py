import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_password(password: str):
    if len(password) < 6:
        raise ValidationError(_("Password must be at least 6 characters long."))

    if not re.search(r'\d', password):
        raise ValidationError(_("Password must contain at least one digit."))

    if not re.search(r'[A-Za-z]', password):
        raise ValidationError(_("Password must contain at least one letter."))
