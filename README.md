# 🎥 Movie Recommender System

A **Content-Based Movie Recommendation System** built with **Python, NLP, and Streamlit**.  
This system suggests movies similar to the one you select, based on their **tags** (overview, genre, keywords, cast, crew).  

---

## 🔹 Features
- ✅ Recommends **Top 5 Similar Movies** to the selected one  
- ✅ Uses **CountVectorizer + Cosine Similarity** for recommendations  
- ✅ Interactive **Streamlit Web App**  
- ✅ Clean and Simple UI  
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
The dataset used in this project is included as [Dataset.zip](https://github.com/nilotpaldhar2004/movie-recommender-system/raw/main/Dataset.zip).  
It contains details like **genres, keywords, cast, crew, and overview** of movies.  

> **Before running the project**, make sure to extract the contents of `Dataset.zip`.  
> The extracted folder includes files like:
> - `tmdb_5000_movies.csv`  
> - `tmdb_5000_credits.csv`

---

## 🔹 How It Works
1. **Movie Input:** User selects or searches for a movie.  
2. **Feature Extraction:** App combines overview, genres, keywords, cast, crew to create a tag vector.  
3. **Similarity Calculation:** Computes cosine similarity between the selected movie and all others.  
4. **Top Recommendations:** App fetches top 5 most similar movies, including poster, rating, and release year.  
5. **Display:** Streamlit shows movies with hover effects, ratings in stars, and release year.  

---

## 🔹 Demo  

<p float="left">
  <img src="https://github.com/nilotpaldhar2004/movie-recommender-system/raw/main/Images/Demo.png" alt="Demo Image 1" width="400"/>
  <img src="https://github.com/nilotpaldhar2004/movie-recommender-system/raw/main/Images/Demo1.png" alt="Demo Image 2" width="400"/>
</p>

---

## 🔹 Installation & Usage

1. **Clone this repository**:
   ```bash
   git clone https://github.com/nilotpaldhar2004/movie-recommender-system.git
   cd movie-recommender-system
   cd movie-recommender-system

