import pickle
import streamlit as st
import requests


st.set_page_config(
    page_title="🎬 Movie Recommender",
    layout="wide"
)

def set_background():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://cdn.wallpapersafari.com/52/29/FkBOyX.jpg");
           
             background-size: cover;
             background-attachment: fixed;
        }
        .block-container {
            backdrop-filter: blur(10px);
            background-color: rgba(255, 255, 255, 0.05);
            border-radius: 12px;
            padding: 2rem;
        }
        h1, h4, p {
            color: white !important;
        }
        .stSelectbox > div > div {
            color: black !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_background()

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    response = requests.get(url).json()
    poster_path = response.get('poster_path')
    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    else:
        return "https://via.placeholder.com/300x450?text=No+Image"


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    
    for i in distances[0:5]:   # include the input movie itself
        movie_id = movies.iloc[i[0]].id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
    
    return recommended_movie_names, recommended_movie_posters



st.markdown("<h1 style='text-align: center;'>🎥 Movie Recommender</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Get recommendations for movies you love, powered by Machine Learning!</h4>", unsafe_allow_html=True)
st.markdown("---")


movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))


movie_list = movies['title'].values
selected_movie = st.selectbox(
    "🎬 Type or select a movie from the dropdown",
    movie_list
)


if st.button("✨ Show Recommendations"):
    names, posters = recommend(selected_movie)
    st.markdown("<h4 style='color:white;'>🎯 Recommended Movies:</h4>", unsafe_allow_html=True)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.image(posters[i], use_column_width=True)
            st.markdown(f"<p style='text-align: center; color: white; font-weight: bold;'>{names[i]}</p>", unsafe_allow_html=True)


st.markdown("---")
st.markdown(
    "<p style='text-align: center; font-size: 12px; color:white;'>👨‍💻 Built by Nilotpal | Powered by Streamlit & TMDB API</p>",
    unsafe_allow_html=True
)
