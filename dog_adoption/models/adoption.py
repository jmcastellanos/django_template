from django.db import models

from django_template.base_models import BaseModel
from dog_adoption.models.dog import Dog
from dog_adoption.models.person import Person


class Adoption(BaseModel):
    """
    Warning: Be careful separating models in distinct files:
    
        In this model we use Dog model and Person model, if we want to use
        Adoption model within Dog or Person model, we will end with a circular
        import and our program will crash. For this case, create another file
        with a function or class, that combines the Adoption model, and the
        Dog or Person model.
    """

    dog: Dog = models.OneToOneField(
        to=Dog,
        on_delete=models.PROTECT,
        related_name="adoption",
    )
    person: Person = models.ForeignKey(
        to=Person,
        on_delete=models.PROTECT,
        related_name="adoptions",
    )
