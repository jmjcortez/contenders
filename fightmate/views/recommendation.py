from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from fightmate.serializers.recommendation import RecommendationListSerializer
from fightmate.models.user import User
from fightmate.functions.user_functions import get_recommended_users

class RecommendationViewSet(ViewSet):

  # temporary
  permission_classes = []
  authentication_classes = []

  def list(self, request, **kwargs):
    recommendations = []
    user = User.objects.get(id=9962)
    print('generating recommendations')
    recommended_user_ids = get_recommended_users(user.id)

    recommended_users = User.objects.filter(id__in=recommended_user_ids)

    for user in recommended_users[:5]:
      main_bio = user.get_latest_bio()

      recommendations.append({
        'email': user.email,
        'first_name': user.first_name,
        'bio_text': main_bio.text if main_bio else 'Random bio to fill in, will change once db finished',
        'disciplines': [ discipline.__dict__ for discipline in user.get_disciplines() ],
        'pkg': user.get_pkg()
      })
    
    num_recommendations = len(recommended_users)

    serializer = RecommendationListSerializer(data={
      'num_recommendations': num_recommendations,
      'recommendations': recommendations
    })
    serializer.is_valid(raise_exception=True)

    return Response(status=status.HTTP_200_OK, data=serializer.data)