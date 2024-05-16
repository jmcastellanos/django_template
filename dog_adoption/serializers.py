"""
Serializers are a practical way to return information from django models

For more information about django_rest_framework serializers visit:
https://www.django-rest-framework.org/api-guide/serializers/
"""

from rest_framework import serializers

from dog_adoption.models import Adoption, Dog, Person


class DogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dog
        fields = ("id", "original_name", "name", "birthday")


class PersonSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, obj: Person):
        """
        This field is created using the instance Person attributes
        If a complex operation is required (ex: interaction with other models)
        is recommended to do it outside the serializer (Serialization occurs once per
        each instance, and could bring latency in the response)
        """
        return obj.first_name + " " + obj.last_name

    class Meta:
        model = Person
        fields = ("id", "birthday", "full_name")


class AdoptionSerializer(serializers.ModelSerializer):
    dog = DogSerializer()
    person = PersonSerializer()

    class Meta:
        model = Adoption
        fields = ("id", "dog", "person")
