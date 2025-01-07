# Import necessary library
import pandas as pd

# Create a sample movie dataset
movies = pd.DataFrame({
    'MovieID': [1, 2, 3, 4, 5],
    'Title': ['The Matrix', 'Toy Story', 'Titanic', 'Inception', 'Shrek'],
    'Genre': ['Action|Sci-Fi', 'Animation|Family', 'Romance|Drama', 'Action|Thriller', 'Animation|Comedy']
})

# Display the dataset
print("Movies Dataset:")
print(movies)

# Define user preferences
user_preferences = ['Action', 'Sci-Fi']

# Function to recommend movies based on user preferences
def recommend_movies(movies, user_preferences):
    recommendations = []
    for _, row in movies.iterrows():
        genres = row['Genre'].split('|')
        # Check if any user preference matches the movie genres
        if any(pref in genres for pref in user_preferences):
            recommendations.append(row['Title'])
    return recommendations

# Get recommendations
recommended_movies = recommend_movies(movies, user_preferences)

# Display recommendations
print("\nUser Preferences:", user_preferences)
print("Recommended Movies:", recommended_movies)
