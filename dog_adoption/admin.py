"""
For more information about django admin visit:
https://docs.djangoproject.com/en/5.0/ref/contrib/admin/
"""

from django.contrib import admin
from dog_adoption.models import Dog, Person


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    pass


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass


