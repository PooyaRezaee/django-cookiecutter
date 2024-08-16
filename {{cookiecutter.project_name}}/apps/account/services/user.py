from django.core.validators import validate_email
from django.db.utils import IntegrityError
from core.logger import logging
from ..models import User
from ..validators import validate_password


def create_user(email: str, password: str) -> User | None:
    validate_email(email)
    validate_password(password)
    
    try:
        return User.objects.create_user(email=email, password=password)
    except IntegrityError:
        logging.info("User creation was repeating")
        return None