from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from fightmate.serializers.recommendation import RecommendationListSerializer
from fightmate.models.user import User


class RecommendationViewSet(ViewSet):

  # temporary
  permission_classes = []
  authentication_classes = []

  def list(self, request, **kwargs):

    users = User.objects.all()[:5]
    recommendations = []

    for user in users:
      main_bio = user.get_latest_bio()

      recommendations.append({
        'email': user.email,
        'first_name': user.first_name,
        'bio_text': main_bio.text if main_bio else 'Random bio to fill in, will change once db finished',
        'disciplines': [ discipline.__dict__ for discipline in user.get_disciplines() ],
        'pkg': user.get_pkg()
      })
    
    num_recommendations = len(users)

    serializer = RecommendationListSerializer(data={
      'num_recommendations': num_recommendations,
      'recommendations': recommendations
    })
    serializer.is_valid(raise_exception=True)

    return Response(status=status.HTTP_200_OK, data=serializer.data)