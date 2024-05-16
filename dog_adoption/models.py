"""
<< DPA Comment >>

In this project we will have dogs and persons (as DB tables/models).

We will simulate an adoption system in which at the beginning we have a dog,
and then a person adopts it, creating an object: Adoption.
This adoption will have a person and a dog, and will be a separated object
in order to keep track of the datetime of the adoption and other possible
details in the adoption.

"""

import datetime
from typing import Optional

from django.db import models

from django_template.base_models import BaseModel


class Dog(BaseModel):
    original_name: str = models.CharField(
        max_length=128,
    )
    name: Optional[str] = models.CharField(
        max_length=128,
        default=None,
        null=True,
    )
    birthday: datetime.date = models.DateField()


class Person(BaseModel):
    birthday: datetime.date = models.DateField()
    first_name: str = models.CharField(
        max_length=254,
    )
    last_name: str = models.CharField(
        max_length=254,
    )
