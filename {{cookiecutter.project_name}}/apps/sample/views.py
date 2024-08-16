from django.shortcuts import HttpResponse
from django.views import View

import random
from core import logger
from .services import created_test_record
from .models import TestData


class SampleView(View):
    def get(self, request):
        logger.debug('this is a {debug} log')
        logger.info('this is a {info} log')
        logger.warning('this is a {warning} log')
        logger.error('this is a {error} log')
        logger.critical('this is a {critical} log')
        
        if random.randint(0,1):
            created_test_record("Test Data")
            logger.info('Data Base added')
        
        return HttpResponse("Hello World")

