import random
from celery import shared_task


@shared_task
def test():
    print(f"Celery Good working {random.randint(11,99)} ...")