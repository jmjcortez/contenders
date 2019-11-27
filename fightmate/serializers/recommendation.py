from rest_framework import serializers

from fightmate.serializers.picture import PictureSerializer


class RecommendationSerializer(serializers.Serializer):

  email = serializers.EmailField()
  first_name = serializers.CharField()
  bio_text = serializers.CharField()
  pictures = PictureSerializer(many=True, allow_null=True)