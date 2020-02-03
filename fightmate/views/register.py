from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from fightmate.serializers.register import RegisterUserSerializer 
from django.db.utils import IntegrityError


class RegisterViewSet(ViewSet):
    
    permission_classes = []
    
    def create(self, request):
        serializer = RegisterUserSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            try:
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)