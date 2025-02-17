import pickle
import streamlit as st
import requests
import pandas as pd

# Replace with your TMDb API v4 Read Access Token
TMDB_ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1ZDdlYzY2ZWJlYmE4MmYzNGQxYzU0MTVlNDgzN2QyYyIsIm5iZiI6MTczOTcyMjUzOS4xMjcsInN1YiI6IjY3YjIwZjJiODAyNzBiMGUwODlmYjc2OSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.TU9hQ7XqHhX7dwvhF5cQktl5FsyjyGmVK6IR72lO-QE"

# Function to fetch movie poster
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    headers = {
        "Authorization": f"Bearer {TMDB_ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for HTTP failures (e.g., 401, 404)
        data = response.json()
        poster_path = data.get("poster_path")

        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"
        else:
            return "https://via.placeholder.com/500x750.png?text=No+Image"  # Default placeholder
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching poster: {e}")
        return "https://via.placeholder.com/500x750.png?text=No+Image"

# Function to recommend movies
def recommend(movie):
    if movie not in movies["title"].values:
        st.error("Movie not found in the dataset.")
        return [], []

    index = movies[movies["title"] == movie].index[0]
    distances = sorted(
        list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1]
    )

    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:  # Get top 5 recommendations
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))

    return recommended_movie_names, recommended_movie_posters

# Streamlit UI
st.title("🎬 Movie Recommendation System")
st.write("Select a movie to get recommendations!")

# Load movie data
movies = pickle.load(open("movie_list.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

# Ensure movies dataframe is a DataFrame (handle any loading issues)
if not isinstance(movies, pd.DataFrame):
    st.error("Error loading movie dataset. Ensure movie_list.pkl is a valid DataFrame.")
    st.stop()

# Dropdown for movie selection
movie_list = movies["title"].values
selected_movie = st.selectbox("🔍 Type or select a movie from the dropdown", movie_list)

# Show recommendations on button click
if st.button("🎥 Show Recommendations"):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

    if recommended_movie_names:
        cols = st.columns(5)
        for i in range(5):
            with cols[i]:
                st.text(recommended_movie_names[i])
                st.image(recommended_movie_posters[i])
    else:
        st.warning("No recommendations found. Try another movie.")