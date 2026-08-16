# 🎬 CineMatch — NLP-Powered Movie Recommender

<div align="center">

[![Live Demo](https://img.shields.io/badge/Demo-Live%20Site-brightgreen?style=for-the-badge&logo=github)](https://nilotpaldhar2004.github.io/movie-recommender-system-main/)
[![Backend](https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge&logo=fastapi)](https://cinematch-ai-recommender.onrender.com)
[![Dataset](https://img.shields.io/badge/Dataset-TMDB%205000-orange?style=for-the-badge)](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)

**A content-based movie recommendation engine built with NLP and cosine similarity.**

[🚀 Try Live Demo](https://nilotpaldhar2004.github.io/movie-recommender-system-main/) · [API Backend](https://cinematch-ai-recommender.onrender.com) · [Portfolio](https://nilotpal-dhar.vercel.app)

</div>

Type any movie title — the system returns 5 films with matching storylines, genres, cast, and cinematic DNA. Deployed as a FastAPI backend on Render with a standalone frontend on GitHub Pages.

---

## 🧠 How It Works

```
User Input (movie title)
        ↓
  Text Vectorization
  (CountVectorizer on tags: genres + cast + crew + overview + keywords)
        ↓
  Cosine Similarity Matrix
  (5000 × 5000, quantized to uint8 for memory efficiency)
        ↓
  Top-5 Nearest Neighbours
  (sorted by similarity score, excluding the input movie)
        ↓
  TMDB API
  (fetches poster, rating, year, genres, overview for each result)
        ↓
  JSON Response → Frontend renders movie cards
```

**Why content-based filtering?**
Unlike collaborative filtering (which requires user rating history), content-based filtering works from day one using only movie metadata — making it ideal for cold-start scenarios and real-time deployment without a database.

---

## ✨ Features

- **Instant autocomplete** — starts from the first character, sorted starts-with first then contains, with keyboard navigation
- **5,000-movie corpus** — trained on the TMDB 5000 Movie Dataset from Kaggle
- **Live TMDB metadata** — posters, ratings, release year, genres, and overviews fetched in real time
- **Selected film card** — shows full details of your searched movie alongside recommendations
- **Hover overlay** — movie overview slides in on poster hover
- **Cinematic UI** — deep indigo-violet gradient background with electric cyan accents
- **Responsive** — 2 columns (mobile) → 3–4 columns (tablet) → 5 columns (desktop)
- **Keep-alive automation** — a scheduled GitHub Actions workflow pings `/ping` to eliminate Render free-tier cold-start delays

---

## 🛠️ Tech Stack

| Layer | Technology |
|:------|:-----------|
| NLP / ML | Scikit-Learn (CountVectorizer, cosine_similarity), NumPy, Joblib |
| Backend | FastAPI, Uvicorn, Requests |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Deployment & CI/CD | Render (backend), GitHub Pages (frontend), GitHub Actions |
| Training | Jupyter Notebook |
| Data | TMDB 5000 Movie Dataset (Kaggle) |
| External API | TMDB (The Movie Database) |

---

## 📂 Project Structure

```
movie-recommender-system/
│
├── main.py                          # FastAPI backend — Render deployment
├── index.html                       # Standalone frontend — GitHub Pages
├── Movie Recommender System.ipynb   # Training notebook — generates model files
├── requirements.txt                 # Python dependencies (pinned)
├── movie_list.pkl                   # Movie metadata DataFrame (~5MB)
├── similarity_quantized.pkl         # Quantized cosine similarity matrix (~23MB)
├── .github/workflows/main.yml       # Scheduled keep-alive ping (GitHub Actions)
├── .gitignore                       # Git ignore rules
├── LICENSE                          # MIT License
└── README.md                        # Project documentation
```

> **Note:** `movie_list.pkl` and `similarity_quantized.pkl` are committed directly to the repository. Combined they're under 30MB — well within GitHub's 100MB file limit — so Render's free tier can load them immediately with zero extra disk configuration.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- pip

### 1. Clone the repository

```bash
git clone https://github.com/nilotpaldhar2004/movie-recommender-system-main.git
cd movie-recommender-system-main
```

### 2. Set up a virtual environment and install dependencies

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Verify the model files

`movie_list.pkl` and `similarity_quantized.pkl` are already included in the repository root alongside `main.py`. If you want to regenerate them yourself, download the [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) and run the training notebook:

```bash
jupyter notebook "Movie Recommender System.ipynb"
```

### 4. Start the FastAPI server

```bash
python main.py
```

Open `http://localhost:10000` — FastAPI serves `index.html` directly.

---

## 🌐 Deployment

| Component | Host | URL |
|:----------|:-----|:----|
| Frontend (`index.html`) | GitHub Pages | https://nilotpaldhar2004.github.io/movie-recommender-system-main/ |
| Backend (`main.py`) | Render | https://cinematch-ai-recommender.onrender.com |

### Backend → Render (free tier)

1. Push your code to GitHub — the `.pkl` model files are committed, not gitignored
2. Go to [render.com](https://render.com) → **New → Web Service → connect your GitHub repo**
3. Set the **Start Command:**
   ```
   python main.py
   ```
4. Set **Environment:** Python 3
5. Deploy — Render will provision the live public URL

> **Keep-alive:** A scheduled [GitHub Actions](https://docs.github.com/en/actions) workflow (`.github/workflows/main.yml`) pings `https://your-app.onrender.com/ping` on a recurring schedule to prevent cold-start delays on Render's free tier — no third-party monitor required.

### Frontend → GitHub Pages

1. Go to your repo → **Settings → Pages → Source → main branch → / (root)**
2. Update the `API_BASE` constant in `index.html`:

```javascript
// In the <script> block at the bottom of index.html:
const API_BASE = (
  window.location.hostname === 'localhost' || ...
) ? 'http://localhost:10000'
  : 'https://cinematch-ai-recommender.onrender.com';
```

3. Commit and push — GitHub Pages deploys within 60 seconds.

---

## 📡 API Reference

### `GET /movies`

Returns all movie titles for the autocomplete dropdown.

```json
{ "count": 4806, "movies": ["Avatar", "Inception", "The Dark Knight", "..."] }
```

### `GET /recommend?movie=Inception&n=5`

Returns top-N content-based recommendations.

**Parameters:**
- `movie` — exact movie title (use `/movies` to browse valid titles)
- `n` — number of results, 1–10 (default: 5)

```json
{
  "query": "Inception",
  "selected": {
    "title": "Inception",
    "poster": "https://image.tmdb.org/t/p/w500/...",
    "rating": 8.3,
    "year": "2010",
    "genres": ["Action", "Science Fiction", "Thriller"],
    "overview": "A thief who steals corporate secrets through dream-sharing..."
  },
  "recommendations": [
    { "title": "Interstellar", "poster": "...", "rating": 8.1, "year": "2014", "genres": ["Adventure", "Drama", "Science Fiction"], "overview": "..." }
  ]
}
```

### `GET /health`

```json
{ "status": "ok", "movies_loaded": true, "model_loaded": true, "total_movies": 4806 }
```

### `GET /ping`

Keep-alive endpoint used by the scheduled GitHub Actions workflow.

```json
{ "pong": true }
```

Full interactive documentation available at `/docs` (Swagger UI) when the server is running.

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

Developed by **Nilotpal Dhar** &nbsp;·&nbsp; [Portfolio](https://nilotpal-dhar.vercel.app) &nbsp;·&nbsp; [LinkedIn](https://www.linkedin.com/in/nilotpal-dhar-24b304294/) &nbsp;·&nbsp; [Kaggle](https://www.kaggle.com/nilotpaldhar)