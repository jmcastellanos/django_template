from rest_framework.response import Response
from rest_framework.views import APIView

from dog_adoption.models import Adoption, Dog, Person
from dog_adoption.serializers import AdoptionSerializer, DogSerializer


class NotAdoptedDogsViews(APIView):

    def get(self, request):
        """
        Retrieves all the dogs that don't have owner yet
        """
        dogs = Dog.objects.filter(adoption__isnull=True)
        data = DogSerializer(instance=dogs, many=True).data

        return Response(data=data)


class DogAdoptionView(APIView):

    def post(self, request, ):
        """
        Creates and adoption
        """
        person_id = request.data["person_id"]
        dog_id = request.data["dog_id"]

        dog = Dog.objects.get(id=dog_id)
        person = Person.objects.get(id=person_id)
        adoption = Adoption(
            dog=dog,
            person=person,
        )
        adoption.save()

        return Response(data={"adoption_id": str(adoption.id)})

    def get(self, request):
        """
        Retrieves all the adoptions
        """
        adoptions = Adoption.objects.all()
        data = AdoptionSerializer(instance=adoptions, many=True,).data
        return Response(data=data)
