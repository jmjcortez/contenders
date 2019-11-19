from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from fightmate.serializers.recommendation import RecommendationSerializer
from fightmate.models.user import User


class RecommendationViewSet(ViewSet):

  permission_classes = []
  authentication_classes = []

  def list(self, request, **kwargs):
    
    #call recommendation function when it's done
    
    #Temporary, looks like shit
    users = User.objects.all()
    data = {
      'users': []
    }
    for user_data in users:
      data['users'].append({
        'email': user_data.email,
        'first_name': user_data.first_name,
      })

    serializer = RecommendationSerializer(data=data)
    serializer.is_valid(raise_exception=True)

    return Response(status=status.HTTP_200_OK, data=serializer.data)