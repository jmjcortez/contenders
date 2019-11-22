import factory

from fightmate.models.user import User


class UserFactory(factory.django.DjangoModelFactory):

  class Meta:
    model = User

  email = factory.Faker('email')
  first_name = factory.Faker('first_name')