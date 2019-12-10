from rest_framework import serializers

from fightmate.models.discipline import Discipline

class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = ('name', )
