from rest_framework.response import Response
from rest_framework.views import APIView

from dog_adoption.models import Dog
from dog_adoption.serializers import DogSerializer


class NotAdoptedDogsViews(APIView):

    def get(self, request):
        """
        Retrieves all the dogs that don't have owner yet
        """
        # filtering dogs
        dogs = Dog.objects.filter(adoption__isnull=True)
        # serializing dogs
        data = DogSerializer(instance=dogs, many=True).data

        return Response(data=data)
