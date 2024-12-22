import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

users_data = pd.read_csv('users_data.csv')
users_df = pd.DataFrame(users_data)

events_data = pd.read_csv('rec_events_data.csv')
events_df = pd.DataFrame(events_data)

def recommend_events(user_id, users_df, events_df):
    user_interests = users_df.loc[users_df['user_id'] == user_id, 'interests'].iloc[0]
    
    vectorizer = CountVectorizer()
    event_category_matrix = vectorizer.fit_transform(events_df['event_category'])
    user_interest_matrix = vectorizer.transform([user_interests])
    similarity = cosine_similarity(user_interest_matrix, event_category_matrix)
    
    events_df['similarity'] = similarity[0]
    recommended_events = events_df.sort_values(by='similarity', ascending=False).head(3)
    return recommended_events[['event_id', 'event_name', 'event_category']]

user_id = 10
recommended = recommend_events(user_id, users_df, events_df)

print("Recommended Events:")
print(recommended)
