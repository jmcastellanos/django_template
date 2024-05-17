"""
Django will look for registered models in the admin.py file
for each application that we have created.
In this example we don't have an admin.py file, so in order
to trick django, we register those models in the __init__.py
file in the admin directory.

Something similar will happen with the models file (see the
__init__.py file in the models directory)
"""

from django.contrib import admin

from dog_adoption.admin.admin_classes import AdoptionAdmin, DogAdmin, PersonAdmin
from dog_adoption.models import Adoption, Dog, Person

admin.site.register(Dog, DogAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Adoption, AdoptionAdmin)
