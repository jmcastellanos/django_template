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
        blank=True,
    )
    birthday: datetime.date = models.DateField()