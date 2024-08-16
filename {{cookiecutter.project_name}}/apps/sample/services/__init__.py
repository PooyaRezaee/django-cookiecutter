import random 
from django.db.models import QuerySet
from ..models import TestData


def created_test_record(content:str) -> TestData:
    TestData.objects.create(
        random_number=random.randint(11111,99999),
        content=content,
    )

def delete_test_reords(list_pk: list[int] | None = None) -> int:
    if list_pk is None:
        return TestData.objects.all().delete()[0]
    else:
        return TestData.objects.filter(pk__in=list_pk).delete()[0]