from rest_framework import serializers

from fightmate.serializers.user import UserSerializer


class RecommendationSerializer(serializers.Serializer):

  users = UserSerializer(many=True, allow_null=True)
