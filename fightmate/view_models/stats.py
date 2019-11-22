class StatsOverviewViewModel(object):
  def __init__(
    self, contenders_nearby_count, contenders_fighting_city_count, contenders_fighting_country_count,
    contenders_global_count, contenders_per_discipline, contenders_per_combat_type
  ):
    self.contenders_nearby_count = contenders_nearby_count #call function
    self.contenders_fighting_city_count = contenders_fighting_city_count
    self.contenders_fighting_country_count = contenders_fighting_country_count
    self.contenders_global_count = contenders_global_count
    self.contenders_per_discipline = contenders_per_discipline
    self.contenders_per_combat_type = contenders_per_combat_type
