from rest_framework import serializers

from fightmate.models.user import User


class StatsOverviewSerializer(serializers.Serializer):

    contenders_nearby_count = serializers.IntegerField() #call function
    contenders_fighting_city_count = serializers.IntegerField()
    contenders_fighting_country_count = serializers.IntegerField()
    contenders_global_count = serializers.IntegerField()
    contenders_per_discipline = serializers.DictField()
    contenders_per_combat_type = serializers.DictField()