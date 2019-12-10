from rest_framework import serializers

from fightmate.serializers.picture import PictureSerializer
from fightmate.serializers.discipline_serializer import DisciplineSerializer

class RecommendationSerializer(serializers.Serializer):

  email = serializers.EmailField()
  first_name = serializers.CharField()
  bio_text = serializers.CharField()
  pictures = PictureSerializer(many=True, allow_null=True, required=False)
  disciplines = DisciplineSerializer(many=True, allow_null=True, required=False)
  pkg = serializers.DictField()

class RecommendationListSerializer(serializers.Serializer):
  recommendations = RecommendationSerializer(many=True)
  num_recommendations = serializers.IntegerField()