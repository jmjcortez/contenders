from rest_framework import serializers

from fightmate.models.user import User

class RegisterUserSerializer(serializers.Serializer):

    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name= serializers.CharField(required=False, allow_blank=True)
    password = serializers.CharField(write_only=True)

    def save(self):
        user = User.objects.create_user(
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'] if self.validated_data.get('last_name', False) else '',
            email=self.validated_data['email'],
            password=self.validated_data['password'],
        )
    
        return user
