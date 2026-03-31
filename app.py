import pickle
import streamlit as st
import requests
import joblib
import numpy as np


st.set_page_config(
    page_title="🎬 Movie Recommender",
    layout="wide"
)


def set_background():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgv4DPVI8S6-6VifnW8JZTEEqpzMAm5X8riOU1Zp2D7ziSvmCxdxX0beLWKNcBAVBD3Ubi0p8zrkkrulO57VWLdN9-W0T0nfDPZeYy9WHxUznwdFIqeppFU0JS2HbFT0zeu82RWCqUTTUhUrEcfYkP_CmgnXl1kCpF76UzL_cFJ0xrFeYuxsiI8gKOT8Q/s1600/NEON-NIGHT-CITY-132023.png");
            background-size: cover;
            background-attachment: fixed;
        }
        .block-container {
            backdrop-filter: blur(6px);
            background-color: rgba(0, 0, 0, 0.4);
            border-radius: 16px;
            padding: 2rem;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.4);
        }
        h1, h4, p {
            color: #f5f5f5 !important;
            text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.6);
        }
        .stSelectbox label {
            color: #fff !important;
            font-weight: bold;
        }
        .stSelectbox > div > div {
            color: black !important;
        }
        .stButton > button {
            background-color: #ff4b4b;
            color: white;
            border-radius: 10px;
            font-weight: bold;
            border: none;
            transition: all 0.3s ease;
        }
        .stButton > button:hover {
            background-color: #ff7878;
            transform: scale(1.05);
        }

        /* Poster Hover + Tooltip */
        .tooltip {
            position: relative;
            display: inline-block;
        }
        .tooltip img {
            border-radius: 12px;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            cursor: pointer;
            width: 100%;
        }
        .tooltip img:hover {
            transform: scale(1.05);
            box-shadow: 0 8px 20px rgba(255, 255, 255, 0.6);
        }
        .tooltip .tooltiptext {
            visibility: hidden;
            width: 140px;
            background-color: rgba(0,0,0,0.8);
            color: #fff;
            text-align: center;
            border-radius: 8px;
            padding: 5px;
            position: absolute;
            z-index: 1;
            bottom: 105%;
            left: 50%;
            margin-left: -70px;
            opacity: 0;
            transition: opacity 0.3s;
            font-size: 12px;
        }
        .tooltip:hover .tooltiptext {
            visibility: visible;
            opacity: 1;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_background()


@st.cache_data
def fetch_poster_info(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    response = requests.get(url).json()
    poster_path = response.get('poster_path')
    release_date = response.get('release_date', 'N/A')
    rating = response.get('vote_average', 0)
    if poster_path:
        poster_url = "https://image.tmdb.org/t/p/w500/" + poster_path
    else:
        poster_url = "https://via.placeholder.com/300x450?text=No+Image"
    return poster_url, release_date, rating

def rating_to_stars(rating):
    rating_out_of_5 = rating / 2
    full_stars = int(rating_out_of_5)
    half_star = 1 if rating_out_of_5 - full_stars >= 0.5 else 0
    empty_stars = 5 - full_stars - half_star
    return "★" * full_stars + "½" * half_star + "☆" * empty_stars


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = list(enumerate(similarity[index]))
    distances = sorted(distances, reverse=True, key=lambda x: x[1])

    recommended_movie_names = []
    recommended_movie_posters = []
    release_dates = []
    ratings = []

    for i in distances[1:6]:  # skip selected movie
        movie_id = movies.iloc[i[0]].id
        poster_url, release_date, rating = fetch_poster_info(movie_id)
        recommended_movie_posters.append(poster_url)
        recommended_movie_names.append(movies.iloc[i[0]].title)
        release_dates.append(release_date)
        ratings.append(rating)

    return recommended_movie_names, recommended_movie_posters, release_dates, ratings


movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = joblib.load('similarity_quantized.pkl').astype(np.float32) / 255


st.markdown("<h1 style='text-align: center;'>🎥 Movie Recommender</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Discover movies you’ll love, powered by Machine Learning!</h4>", unsafe_allow_html=True)
st.markdown("---")

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "🎬 Type or select a movie from the dropdown",
    movie_list
)


if st.button("✨ Show Recommendations"):

    rec_names, rec_posters, rec_years, rec_ratings = recommend(selected_movie)

    selected_index = movies[movies['title'] == selected_movie].index[0]
    selected_id = movies.iloc[selected_index].id
    selected_poster, selected_year, selected_rating = fetch_poster_info(selected_id)

    names = [selected_movie] + rec_names
    posters = [selected_poster] + rec_posters
    years = [selected_year] + rec_years
    ratings = [selected_rating] + rec_ratings

    st.markdown("<h4 style='color:white;'>🎯 Movies You May Like:</h4>", unsafe_allow_html=True)
    cols = st.columns(6, gap="small")
    for i in range(6):
        stars = rating_to_stars(ratings[i])
        with cols[i]:
            st.markdown(f"""
                <div class="tooltip">
                    <img src="{posters[i]}" alt="{names[i]}">
                    <span class="tooltiptext">{stars} | {years[i][:4]}</span>
                </div>
                <p style='text-align:center; color:white; font-weight:bold; margin-top:4px;'>{names[i]}</p>
            """, unsafe_allow_html=True)


st.markdown("---")
st.markdown(
    "<p style='text-align: center; font-size: 12px; color:#ddd;'>👨‍💻 Built by <b>Nilotpal Dhar</b> | Powered by Streamlit & TMDB API</p>",
    unsafe_allow_html=True
)
