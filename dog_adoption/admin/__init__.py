from django.contrib import admin

from dog_adoption.admin.admin_classes import AdoptionAdmin, DogAdmin, PersonAdmin
from dog_adoption.models import Adoption, Dog, Person

admin.site.register(Dog, DogAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Adoption, AdoptionAdmin)
