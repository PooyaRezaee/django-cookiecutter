from django.contrib import admin
from .models import TestData


@admin.register(TestData)
class TestAdmin(admin.ModelAdmin):
    pass

