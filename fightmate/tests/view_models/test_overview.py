from django.test import TestCase

from fightmate.view_models.stats import StatsOverviewViewModel


class StatsOverviewViewModelTest(TestCase):

  def test_returns_correct_attributes(self):
    payload = {
      'contenders_nearby_count': 1,
      'contenders_fighting_city_count': 1,
      'contenders_fighting_country_count': 1,
      'contenders_global_count': 1,
      'contenders_per_discipline': {
        'test': 1
      },
      'contenders_per_combat_type': {
        'test': 1
      },
    }

    vm = StatsOverviewViewModel(
      contenders_nearby_count=1,
      contenders_fighting_city_count=1,
      contenders_fighting_country_count=1,
      contenders_global_count=1,
      contenders_per_discipline={
        'test': 1
      },
      contenders_per_combat_type={
        'test': 1
      }
    )

    self.assertDictEqual(payload, {
      'contenders_nearby_count': vm.contenders_nearby_count,
      'contenders_fighting_city_count': vm.contenders_fighting_city_count,
      'contenders_fighting_country_count': vm.contenders_fighting_country_count,
      'contenders_global_count': vm.contenders_global_count,
      'contenders_per_discipline': vm.contenders_per_discipline,
      'contenders_per_combat_type': vm.contenders_per_combat_type,
    })