from rest_framework import serializers

from fightmate.models.bio import Pictures


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('is_main', 'url')