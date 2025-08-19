from rest_framework import serializers

from mainapp.serializers import CartSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    cart = CartSerializer(read_only=True)

    class Meta:
        model = User
        fields = "__all__"
