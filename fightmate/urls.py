from django.urls import path, include
from rest_framework.routers import DefaultRouter
from fightmate.views.user import UserViewSet
from fightmate.views.register import RegisterViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()

router.register(r'user', UserViewSet, base_name='User')
router.register(r'register', RegisterViewSet, base_name='Register')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]