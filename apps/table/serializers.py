from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework import serializers
from .models import User


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "phone", "avatar")
