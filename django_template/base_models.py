import datetime
import uuid

from django.db import models


class BaseModel(models.Model):
    """
    Abstract model will be the base (skeleton)
    for future models
    """
    id: uuid.UUID = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    creation_datetime: datetime.datetime = models.DateTimeField(
        auto_now_add=True,
    )
    last_modified_datetime: datetime.datetime = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        abstract = True
