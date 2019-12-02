from django.test import TestCase

from fightmate.serializers.recommendation import RecommendationListSerializer


class RecommendationListSerializerTest(TestCase):

    def test_serializes(self):
        payload = [{
            'num_recommendations': 1, 
            'recommendations': [{
                'email': 'test@test.com',
                'first_name': 'test',
                'bio_text': 'text',
                'first_name': 'test'
            }]    
        }]

        serializer = RecommendationListSerializer(data=payload)
        self.assertFalse(serializer.is_valid())