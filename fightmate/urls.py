from django.urls import path, include
from rest_framework.routers import DefaultRouter
from fightmate.views.user_viewset import UserViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'user', UserViewSet, base_name='User')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]