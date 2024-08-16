from ..models import User


def count_users() -> int:
    return User.objects.count()