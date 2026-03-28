# 🎬 Movie Recommender System

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit"/>
  <img src="https://img.shields.io/badge/NLP-Scikit--Learn-orange?style=for-the-badge" alt="NLP"/>
  <img src="https://img.shields.io/badge/API-TMDB-01b4e4?style=for-the-badge&logo=the-movie-database&logoColor=white" alt="TMDB"/>
</p>

<p align="center">
  <a href="https://github.com/nilotpaldhar2004/movie-recommender-system/stargazers"><img src="https://img.shields.io/github/stars/nilotpaldhar2004/movie-recommender-system?style=social" alt="Stars"/></a>
  <a href="https://github.com/nilotpaldhar2004/movie-recommender-system/blob/main/LICENSE"><img src="https://img.shields.io/github/license/nilotpaldhar2004/movie-recommender-system?color=blue" alt="License"/></a>
  <a href="https://github.com/nilotpaldhar2004/movie-recommender-system/commits/main"><img src="https://img.shields.io/github/last-commit/nilotpaldhar2004/movie-recommender-system" alt="Last Commit"/></a>
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
3. **Vectorization:** Converting text tags into a 5000-dimensional vector space using Bag-of-Words.
4. **Similarity Engine:** Calculating the distance between movie vectors using the Cosine Similarity formula:
   $$similarity = \cos(\theta) = \frac{A \cdot B}{\|A\| \|B\|}$$
5. **UI Rendering:** Fetching high-resolution posters via API calls to the TMDB database based on `movie_id`.

---

## 🔹 Features
- 📊 **Dynamic Search:** Predictive search bar to select from 5,000+ titles.
- 🖼️ **Poster Integration:** Real-time fetching of movie artwork via API.
- ⭐ **Detailed Metadata:** Displays ratings and release years alongside recommendations.
- 📱 **Responsive UI:** Clean, mobile-friendly interface with hover animations.

---

## 🔹 Dataset
The project utilizes the **TMDB 5000 Movie Dataset**. 
- Download: [Dataset.zip](https://github.com/nilotpaldhar2004/movie-recommender-system/raw/main/Dataset.zip)
- *Note:* Ensure `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv` are in the project root before execution.

---

## 🔹 Installation & Local Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/nilotpaldhar2004/movie-recommender-system.git](https://github.com/nilotpaldhar2004/movie-recommender-system.git)
   cd movie-recommender-system
## Install Dependencies:

Bash
pip install -r requirements.txt
## Run the Application:

Bash
streamlit run app.py
##🔹 License
Distributed under the MIT License. See LICENSE for more information.

Developed by Nilotpal Dhar • March 2026


---

### ⚖️ Adding the MIT License (Professional Standard)
Follow these steps to commit the license today:

1.  In your GitHub Repo, click **Add file** -> **Create new file**.
2.  Name it `LICENSE`.
3.  Click **Choose a license template** on the right.
4.  Select **MIT License**.
5.  Click **Review and submit** (it will automatically add your name and 2026).
6.  **Commit** the file with the message: `docs: add MIT license`.

### 💡 Why this is better:
* **Math Inclusion:** Adding the LaTeX formula for **Cosine Similarity** proves you actually understand the underlying machine learning.
* **API Mention:** Explicitly mentioning the TMDB API shows you can work with external data sources.
* **Better Badges:** I switched them to `for-the-badge` style, which is larger and more modern.

**Would you like me to help you create a "Requirements.txt" file that matches this setup exactly?
