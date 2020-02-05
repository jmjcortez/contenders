def get_recommended_users(user_id):
    
    import pandas as pd
    import pandas.io.sql as sql
    from sqlalchemy import create_engine

    def contenders_connection():
        conn_contenders = create_engine(
            'postgresql://{}:{}@{}:{}/{}'.format(
                'postgres',
                'jared123',
                'contenders2.cmgazgvkzrel.us-east-2.rds.amazonaws.com',
                5432,
                'contenders'
            )
        )

        return conn_contenders

     # conn_contenders = contenders_connection()
    
    q = """ select a.id,
               date(a.date_of_birth) as dob,
               extract(YEAR from now() ) - extract(YEAR from a.date_of_birth ) as age,
               a.weight,
               a.height,
               a.gender,
               a.city_id,
               a.country_id,
               c.id as discipline_id,
               c.grapple,
               c.kick,
               c.punch
               
        from fightmate_user as a
        left join
             user_discipline as b on a.id=b.user_id
        left join
             discipline as c on b.discipline_id = c.id
        where a.id = {}
        limit 10
         """.format(user_id)
    user = pd.read_sql(q, contenders_connection())
    
    q = """ select a.id,
               date(a.date_of_birth) as dob,
               extract(YEAR from now() ) - extract(YEAR from a.date_of_birth ) as age,
               a.weight,
               a.height,
               a.gender,
               c.id as discipline_id
               
        from fightmate_user as a
        left join
             user_discipline as b on a.id=b.user_id
        left join
             discipline as c on b.discipline_id = c.id
        where a.city_id = {} and
              a.country_id = {} and
              c.grapple = {} and
              c.kick = {} and
              c.punch = {} and
              a.gender = '{}' and
              a.id != {}
         """.format(user['city_id'][0], 
                    user['country_id'][0],
                    user['grapple'][0],
                    user['kick'][0],
                    user['punch'][0],
                    user['gender'][0],
                    user['id'][0])
    similar_users = pd.read_sql(q, contenders_connection())
    similar_users = similar_users.sample(frac=1)
    
    return list(similar_users['id'])