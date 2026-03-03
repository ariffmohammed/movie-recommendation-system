import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Movie ratings by users
data = {
    'Inception': [5, 4, 0, 0, 1],
    'Interstellar': [4, 5, 0, 0, 2],
    'The Dark Knight': [5, 4, 4, 0, 0],
    'Titanic': [0, 0, 0, 5, 4],
    'The Notebook': [0, 0, 1, 4, 5],
    'Avengers': [4, 0, 5, 0, 0],
    'Iron Man': [3, 0, 5, 0, 0],
}

df = pd.DataFrame(data)

similarity = cosine_similarity(df.T)
similarity_df = pd.DataFrame(similarity, index=df.columns, columns=df.columns)

def recommend(movie, n=3):
    scores = similarity_df[movie].sort_values(ascending=False)
    scores = scores.drop(movie)
    return scores.head(n)
    
print(recommend('Interstellar'))
print(recommend('Titanic'))

