from rest_framework import serializers

from dog_adoption.models import Person


class PersonSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, obj: Person):
        """
        This field is created using the instance Person attributes
        If a complex operation is required (ex: interaction with other models)
        is recommended to do it outside the serializer (Serialization occurs once per
        each instance, and could bring latency in the response)
        """
        return obj.full_name

    class Meta:
        model = Person
        fields = ("id", "birthday", "full_name")
