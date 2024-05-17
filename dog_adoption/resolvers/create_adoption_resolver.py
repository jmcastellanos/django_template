from dog_adoption.models import Adoption, Dog, Person


class CreateAdoptionResolver:
    """
    << DPA Comment >>:
    This class will encapsulate the functionality that is used in the view.
    Now you can call this class in other views, scripts or if we use another
    technology like graphql.

    The name "resolver" is only a standard that I'm used to, but maybe it's
    not the correct way to call to this type of classes.
    """

    def resolve(
        self,
        dog_id: str,  # it could also be a dog object directly
        person_id: str,  # it could also be a person object directly
    ) -> Adoption:
        dog = Dog.objects.get(id=dog_id)
        person = Person.objects.get(id=person_id)
        adoption = Adoption(
            dog=dog,
            person=person,
        )
        adoption.save()
        return adoption
