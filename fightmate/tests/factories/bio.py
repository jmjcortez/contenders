import factory

from fightmate.models.bio import Bio
from fightmate.tests.factories.user import UserFactory


class BioFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Bio

    user = UserFactory()
    time_state = factory.Faker('date_time')
    text =  factory.Faker('profile')
    is_last = True
