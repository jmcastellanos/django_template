from http import HTTPStatus

from rest_framework.response import Response
from rest_framework.views import APIView

from dog_adoption.models import Adoption
from dog_adoption.resolvers.create_adoption_resolver import CreateAdoptionResolver
from dog_adoption.serializers.adoption_serializer import AdoptionSerializer


class DogAdoptionView(APIView):

    def post(self, request, ):
        """
        Creates and adoption using a resolver.
        """
        resolver = CreateAdoptionResolver()
        adoption = resolver.resolve(
            person_id=request.data["person_id"],
            dog_id=request.data["dog_id"],
        )

        return Response(
            data={"adoption_id": str(adoption.id)},
            status=HTTPStatus.CREATED,
        )

    def get(self, request):
        """
        Retrieves all the adoptions
        """
        adoptions = Adoption.objects.all()
        data = AdoptionSerializer(instance=adoptions, many=True,).data
        return Response(data=data)
