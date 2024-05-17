from rest_framework import serializers

from dog_adoption.models import Adoption
from dog_adoption.serializers.dog_serializer import DogSerializer
from dog_adoption.serializers.person_serializer import PersonSerializer


class AdoptionSerializer(serializers.ModelSerializer):
    dog = DogSerializer()
    person = PersonSerializer()

    class Meta:
        model = Adoption
        fields = ("id", "dog", "person")
