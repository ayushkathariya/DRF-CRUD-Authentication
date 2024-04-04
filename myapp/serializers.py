from rest_framework.serializers import ModelSerializer
from .models import CustomUser, Todo
from rest_framework import serializers


class CustomUserSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)
    date_joined = serializers.DateTimeField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ["id", "email", "password", "date_joined"]

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data["email"], password=validated_data["password"]
        )
        return user


class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"
        extra_kwargs = {"user": {"required": False}}
