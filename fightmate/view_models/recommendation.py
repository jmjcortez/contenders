from fightmate.models.user import User


class RecommendationListViewModel(object):
  def __init__(self):
    
    users = User.objects.all()
    
    self.recommendations = []
    self.num_recommendations = 0
    
    for user in users:
      main_bio = user.get_latest_bio()

      data['recommendations'].append({
        'email': user.email,
        'first_name': user.first_name,
        'bio_text': main_bio.text,
      })
