from rest_framework import serializers

from api.models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = [
            "name",
            "mpg",
            "cylinders",
            "displacement",
            "horsepower",
            "weight",
            "acceleration",
            "model",
            "origin",
        ]
