# 🎥 Movie Recommender System

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)  
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit&logoColor=white)  
![GitHub stars](https://img.shields.io/github/stars/nilotpaldhar2004/movie-recommender-system?style=social&cacheSeconds=300)
<!-- GitHub Repository Badges -->
<p align="center">
  <a href="https://github.com/nilotpaldhar2004/movie-recommender-system/stargazers">
    <img src="https://img.shields.io/github/stars/nilotpaldhar2004/movie-recommender-system?style=social&cacheSeconds=300" alt="GitHub stars"/>
  </a>
  <a href="https://github.com/nilotpaldhar2004/movie-recommender-system/network/members">
    <img src="https://img.shields.io/github/forks/nilotpaldhar2004/movie-recommender-system?style=social&cacheSeconds=300" alt="GitHub forks"/>
  </a>
  <a href="https://github.com/nilotpaldhar2004/movie-recommender-system/issues">
    <img src="https://img.shields.io/github/issues/nilotpaldhar2004/movie-recommender-system" alt="GitHub issues"/>
  </a>
  <a href="https://github.com/nilotpaldhar2004/movie-recommender-system/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/nilotpaldhar2004/movie-recommender-system" alt="License"/>
  </a>
  <a href="https://github.com/nilotpaldhar2004/movie-recommender-system/commits/main">
    <img src="https://img.shields.io/github/last-commit/nilotpaldhar2004/movie-recommender-system" alt="Last Commit"/>
  </a>
</p>

A **Content-Based Movie Recommendation System** built with **Python, NLP, and Streamlit**.  
This system suggests movies similar to the one you select, based on **tags** (overview, genre, keywords, cast, crew).  

---

## 🔹 Features
- ✅ Recommends **Top 5 Similar Movies**  
- ✅ Uses **CountVectorizer + Cosine Similarity**  
- ✅ Interactive **Streamlit Web App**  
- ✅ Clean and simple UI  
- ✅ Deployable on **Streamlit Cloud**  

---

## 🔹 Tech Stack
- **Python**
- **Pandas / NumPy**
- **scikit-learn** (CountVectorizer, Cosine Similarity)
- **Streamlit** (for UI)
- **Requests** (for fetching posters from TMDB API)

---

## 🔹 Dataset
Download the dataset here: [Dataset.zip](https://github.com/nilotpaldhar2004/movie-recommender-system/raw/main/Dataset.zip).  
It contains **genres, keywords, cast, crew, and overview** of movies.  

**Note:** Extract the contents of `Dataset.zip` before running the project.  
Included files:
- `tmdb_5000_movies.csv`  
- `tmdb_5000_credits.csv`

---

## 🔹 How It Works

1. **Movie Input:** User selects or searches for a movie.  
2. **Feature Extraction:** App combines **overview, genres, keywords, cast, crew** to create a tag vector.  
3. **Similarity Calculation:** Computes **cosine similarity** between selected movie and all others.  
4. **Top Recommendations:** App fetches **top 5 most similar movies**, including poster, rating, and release year.  
5. **Display:** Streamlit shows movies with hover effects and ratings in stars.  


---

## 🔹 Demo  

<p float="left">
  <img src="https://github.com/nilotpaldhar2004/movie-recommender-system/raw/main/Images/Demo.png" alt="Demo Image 1" width="400"/>
  <img src="https://github.com/nilotpaldhar2004/movie-recommender-system/raw/main/Images/Demo1.png" alt="Demo Image 2" width="400"/>
</p>

---

## 🔹 Live Demo

Try it here:  

[🎬 Open Movie Recommender App](https://movie-recommender-system-cma4qjqed65yausybn4vrd.streamlit.app/)

---

## 🔹 Installation & Usage

1. **Clone repository:**
   ```bash
   git clone https://github.com/nilotpaldhar2004/movie-recommender-system.git
   cd movie-recommender-system

