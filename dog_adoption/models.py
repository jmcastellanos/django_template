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
