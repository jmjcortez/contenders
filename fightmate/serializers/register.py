from rest_framework import serializers

from fightmate.models.user import User

class RegisterUserSerializer(serializers.Serializer):

    email = serializers.EmailField()
    first_name = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def save(self):
        user = User.objects.create_user(
            first_name=self.validated_data['first_name'],
            email=self.validated_data['email'],
            password=self.validated_data['password']
        )
    
        return user
