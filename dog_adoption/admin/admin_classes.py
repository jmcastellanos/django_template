"""
For more information about django admin visit:
https://docs.djangoproject.com/en/5.0/ref/contrib/admin/

Depending on how big this classes are, you can separate them in different files.
"""

from django.contrib import admin

from dog_adoption.models import Person


class DogAdmin(admin.ModelAdmin):
    list_display = ["original_name", "name"]


class PersonAdmin(admin.ModelAdmin):
    list_display = ["full_name"]

    def get_full_name(self, obj: Person) -> str:
        return obj.full_name


class AdoptionAdmin(admin.ModelAdmin):
    pass
