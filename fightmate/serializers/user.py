from rest_framework import serializers

from fightmate.models.user import User


class UserSerializer(serializers.Serializer):
  
  email = serializers.EmailField()
  first_name = serializers.CharField()