from django.contrib import admin
from .models import *
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass
