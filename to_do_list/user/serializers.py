from rest_framework import serializers
from user.models import (
    User
)



class UserSerializer(serializers.Serializer):
    password = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['id']

class LoginSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['email','password']