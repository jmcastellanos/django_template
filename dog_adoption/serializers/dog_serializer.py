"""
Serializers are a practical way to return information from django models

For more information about django_rest_framework serializers visit:
https://www.django-rest-framework.org/api-guide/serializers/
"""

from rest_framework import serializers

from dog_adoption.models import Dog


class DogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dog
        fields = ("id", "original_name", "name", "birthday")
