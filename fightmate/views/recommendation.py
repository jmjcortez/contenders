from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from fightmate.serializers.recommendation import RecommendationListSerializer
from fightmate.view_models.recommendation import RecommendationListViewModel
from fightmate.models.user import User


class RecommendationViewSet(ViewSet):

  # temporary
  permission_classes = []
  authentication_classes = []

  def list(self, request, **kwargs):
    #call recommendation function when it's done
    
    vm = RecommendationListViewModel()

    serializer = RecommendationListSerializer(data=vm.__dict__)
    serializer.is_valid(raise_exception=True)

    return Response(status=status.HTTP_200_OK, data=serializer.data)