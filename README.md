# 🎬 Movie Recommender System

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit"/>
  <img src="https://img.shields.io/badge/NLP-Scikit--Learn-orange?style=for-the-badge" alt="NLP"/>
  <img src="https://img.shields.io/badge/API-TMDB-01b4e4?style=for-the-badge&logo=the-movie-database&logoColor=white" alt="TMDB"/>
</p>

<p align="center">
  <a href="https://github.com/nilotpaldhar2004/movie-recommender-system/stargazers">
    <img src="https://img.shields.io/github/stars/nilotpaldhar2004/movie-recommender-system?style=for-the-badge&logo=github&color=yellow" alt="Stars"/>
  </a>
  <a href="https://github.com/nilotpaldhar2004/movie-recommender-system/network/members">
    <img src="https://img.shields.io/github/forks/nilotpaldhar2004/movie-recommender-system?style=for-the-badge&logo=github&color=blue" alt="Forks"/>
  </a>
</p>

<p align="center">
  <b>If you find this project helpful, please consider giving it a ⭐ to show your support!</b>
</p>

An intelligent **Content-Based Movie Recommendation Engine** that utilizes Natural Language Processing (NLP) to suggest movies based on metadata similarity.

🚀 **Live Demo:** [🎬 Open Movie Recommender App](https://movie-recommender-system-cma4qjqed65yausybn4vrd.streamlit.app/)

---

## 🔹 Project Overview
This system implements a vector-space model to find similarities between over 5,000 movies. By processing text data (genres, cast, crew, and overviews), it converts movies into vectors and uses **Cosine Similarity** to recommend the top 5 closest matches.

### 🛠️ Tech Stack
- **Engine:** Python, Pandas, NumPy
- **Machine Learning:** Scikit-Learn (`CountVectorizer`, `Cosine Similarity`)
- **Frontend:** Streamlit (Custom CSS & UI components)
- **Data Source:** TMDB API (for real-time poster fetching)

---

## ⚙️ How It Works (The Pipeline)

1. **Data Preprocessing:** Merging `tmdb_5000_movies` and `tmdb_5000_credits` datasets.
2. **Tag Generation:** Stemming and cleaning metadata (Overview + Genre + Keywords + Cast + Crew).
3. **Vectorization:** Converting text tags into a 5,000-dimensional vector space using Bag-of-Words.
4. **Similarity Engine:** Calculating the distance between movie vectors using the Cosine Similarity formula:
   $$similarity = \cos(\theta) = \frac{A \cdot B}{\|A\| \|B\|}$$
5. **UI Rendering:** Fetching high-resolution posters via API calls to the TMDB database based on `movie_id`.

---

## 🔹 Installation & Local Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/nilotpaldhar2004/movie-recommender-system.git
   cd movie-recommender-system


1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   streamlit run app.py
---


📈 Project Insights
<p align="center">
<a href="https://star-history.com/#nilotpaldhar2004/movie-recommender-system&Date">
<img src="https://api.star-history.com/svg?repos=nilotpaldhar2004/movie-recommender-system&theme=dark" alt="Star History Chart" width="600"/>
</a>
</p>
<p align="center">
<i>Track the growth of this project over time!</i>
</p>

---

🔹 License
Distributed under the MIT License. See LICENSE for more information.
---
Developed by Nilotpal Dhar • March 2026
