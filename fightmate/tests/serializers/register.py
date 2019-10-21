import factory

from django.test import TestCase

from fightmate.models.user import User
from fightmate.serializers.register import RegisterUserSerializer

###
###  MODIFY THE DB FOR TEST
###
class RegisterUserSerializerTest(TestCase):

    def test_serializes(self):
        
        data = {
            "email": "test@email.com",
            "password": "password",
            "first_name": "firstname"
        }

        serializer = RegisterUserSerializer(data=data)

        self.assertTrue(serializer.is_valid())
    
    def test_saves(self):

        data = {
            "email": "test@email.com",
            "password": "password",
            "first_name": "firstname"
        }

        serializer = RegisterUserSerializer(data=data)

        user = User.objects.get(email="test@email.com")

        ###assert user exists