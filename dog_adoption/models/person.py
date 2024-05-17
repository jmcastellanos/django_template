import datetime

from django.db import models

from django_template.base_models import BaseModel


class Person(BaseModel):
    birthday: datetime.date = models.DateField()
    first_name: str = models.CharField(
        max_length=254,
    )
    last_name: str = models.CharField(
        max_length=254,
    )

    @property
    def full_name(self) -> str:
        return self.first_name + ' ' + self.last_name
