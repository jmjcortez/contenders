from django import urls

from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from fightmate.tests.factories.user import UserFactory


class StatsViewSetTest(APITestCase):

  def setUp(self):
    self.user = UserFactory()

    self.url = urls.reverse('stats-overview')
    self.client = APIClient()
    self.client.force_authenticate(self.user)

  def test_url_exists(self):
    self.assertEqual(self.url, '/api/stats/overview/')    
  
  def test_view_returns_200(self):
    response = self.client.get(self.url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)   