import pandas as pd

import graphlab

u_cols = ['user_id','age','sex','occupation','zip_code']

users = pd.read_csv('ml-100k/u.user',sep='|',names=u_cols,encoding='latin-1')

r_cols = ['user_id','movie_id','rating','unix_timestamp']

ratings = pd.read_csv('ml-100k/u.data',sep='\t',names=r_cols,encoding='latin-1')

i_cols = ['movie id', 'movie title' ,'release date','video release date', 'IMDb URL', 'unknown', 'Action', 'Adventure','Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy','Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']

items = pd.read_csv('ml-100k/u.item',sep='|',names=i_cols,encoding='latin-1')

#print users.shape

#print users.head()

#print ratings.shape

#print ratings.head()

#print items.shape

#print items.head()

ratings_base = pd.read_csv('ml-100k/ub.base',sep='\t',names=r_cols,encoding='latin-1')

ratings_test = pd.read_csv('ml-100k/ub.test',sep='\t',names=r_cols,encoding='latin-1')

#print ratings_base.shape 

#print ratings_test.shape

train_data = graphlab.SFrame(ratings_base)

test_data = graphlab.SFrame(ratings_test)

popularity_model = graphlab.popularity_recommender.create(train_data,user_id='user_id',item_id='movie_id',target='rating')

popularity_recomm = popularity_model.recommend(users=range(1,6),k=5)

popularity_recomm.print_rows(num_rows=25)

#print ratings_base.groupby(by='movie_id')['rating'].mean().sort_values(ascending=False).head(20)

model_performance = graphlab.compare(test_data, [popularity_model])

graphlab.show_comparison(model_performance,[popularity_model])