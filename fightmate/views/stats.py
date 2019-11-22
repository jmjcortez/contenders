from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from fightmate.view_models.stats import StatsOverviewViewModel


class StatsViewSet(ViewSet):

  # temporary
  permission_classes = []
  authentication_classes = []

  @action(detail=False, url_path='overview')
  def overview(self, request):


    return Response(status=status.HTTP_200_OK)