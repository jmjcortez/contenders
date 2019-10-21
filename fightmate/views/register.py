from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from fightmate.serializers.register import RegisterUserSerializer 

class RegisterViewSet(ViewSet):
    def create(self, request):
        pass
        serializer = RegisterUserSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)