# 🎥 Movie Recommender System

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)  
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit&logoColor=white)  
![GitHub stars](https://img.shields.io/github/stars/nilotpaldhar2004/movie-recommender-system?style=social)  

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

<p align="center">
  <img src="Images/FlowDiagram.png" alt="How It Works Diagram" width="600"/>
</p>

---

## 🔹 Demo  

<p float="left">
  <img src="Images/Demo.gif" alt="Live Demo GIF" width="400"/>
  <img src="Images/Demo1.png" alt="Static Demo Image" width="400"/>
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

