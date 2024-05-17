"""
<< DPA Comment >>

In this project we will have dogs and persons (as DB tables/models).

We will simulate an adoption system in which at the beginning we have a dog,
and then a person adopts it, creating an object: Adoption.
This adoption will have a person and a dog, and will be a separated object
in order to keep track of the datetime of the adoption and other possible
details in the adoption.

"""

from dog_adoption.models.dog import Dog
from dog_adoption.models.person import Person
from dog_adoption.models.adoption import Adoption
