from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from fightmate.view_models.stats import StatsOverviewViewModel
from fightmate.serializers.stats import StatsOverviewSerializer

class StatsViewSet(ViewSet):

  # temporary
  permission_classes = []
  authentication_classes = []

  @action(detail=False, url_path='overview')
  def overview(self, request):

    # put all your logic in VM, kasi ano pang purpose nito duh
    vm = StatsOverviewViewModel(
      contenders_nearby_count=54, #call function
      contenders_fighting_city_count=321,
      contenders_fighting_country_count=7681,
      contenders_global_count=75213,
      contenders_per_discipline={
        'kick': 1,
        'punch': 32,
        'grapple': 123
      },
      contenders_per_combat_type={
        'MMA': 21,
        'Muay Thai': 312,
        'Boxing': 91,
        'Karate': 12,
        'Taekwondo': 42,
      }
    )

    serializer = StatsOverviewSerializer(data=vm.__dict__)
    serializer.is_valid(raise_exception=True)

    return Response(status=status.HTTP_200_OK, data=serializer.data)