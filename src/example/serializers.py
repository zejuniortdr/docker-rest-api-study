from rest_framework import serializers

from .models import Example


class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = ("id", "number", "short_text", "long_text", "some_date", "boolean")
