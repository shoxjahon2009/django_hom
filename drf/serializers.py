from rest_framework import serializers
from rest_framework.response import Response

from .models import Person


class PoetSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Person
        fields = "all"