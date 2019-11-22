from django.urls import path, include
from rest_framework.routers import DefaultRouter
from fightmate.views.user import UserViewSet
from fightmate.views.register import RegisterViewSet
from fightmate.views.recommendation import RecommendationViewSet
from fightmate.views.stats import StatsViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()

router.register(r'user', UserViewSet, base_name='user')
router.register(r'register', RegisterViewSet, base_name='register')
router.register(r'recommendation', RecommendationViewSet, base_name='recommendation')
router.register(r'stats', StatsViewSet, base_name='stats')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]