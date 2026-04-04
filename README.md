# 🎬 CineMatch — NLP-Powered Movie Recommender

[![Live Demo](https://img.shields.io/badge/Demo-Live%20Site-brightgreen?style=for-the-badge&logo=github)](https://nilotpaldhar2004.github.io/movie-recommender-system/)
[![Backend](https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Dataset](https://img.shields.io/badge/Dataset-TMDB%205000-orange?style=for-the-badge)](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)

A content-based movie recommendation engine built with NLP and cosine similarity. Type any movie title — the system returns 5 films with matching storylines, genres, cast, and cinematic DNA. Deployed as a FastAPI backend on Render with a standalone frontend on GitHub Pages.

🚀 **[Try the Live Demo](https://nilotpaldhar2004.github.io/movie-recommender-system/)**

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
- **Keep-alive endpoint** — `/ping` prevents Render free-tier cold-start delays

---

## 🛠️ Tech Stack

| Layer | Technology |
|:------|:-----------|
| NLP / ML | Scikit-Learn (CountVectorizer, cosine\_similarity) |
| Backend | FastAPI, Uvicorn, Requests |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Deployment | Render (backend) + GitHub Pages (frontend) |
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
├── LICENSE                          # MIT License
├── README.md                        # Project documentation
│
└── (gitignored — not committed)
    ├── movie_list.pkl               # Movie metadata DataFrame (~5MB)
    ├── similarity_quantized.pkl     # Quantized cosine similarity matrix (~23MB)
    └── Dataset.zip                  # Raw TMDB dataset (download from Kaggle)
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- ~500MB disk space for model files

### 1. Clone the repository

```bash
git clone https://github.com/nilotpaldhar2004/movie-recommender-system.git
cd movie-recommender-system
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Download the dataset

Download the TMDB 5000 Movie Dataset from Kaggle and place it in the project root:

```
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata
```

### 4. Generate model files

Open and run the Jupyter notebook to produce `movie_list.pkl` and `similarity_quantized.pkl`:

```bash
jupyter notebook "Movie Recommender System.ipynb"
```

Run all cells — this generates both model files in the project root.

### 5. Start the FastAPI server

```bash
uvicorn main:app --reload --port 8000
```

Open `http://localhost:8000` — FastAPI serves `index.html` directly.

---

## 🌐 Deployment

### Backend → Render (free tier)

1. Push your code to GitHub — `.pkl` files and `Dataset.zip` are gitignored, **do not commit them**
2. Go to [render.com](https://render.com) → **New → Web Service → connect your GitHub repo**
3. Set the **Start Command:**
   ```
   uvicorn main:app --host 0.0.0.0 --port $PORT
   ```
4. Set **Environment:** Python 3
5. Upload `movie_list.pkl` and `similarity_quantized.pkl` using **Render Disk** (persistent storage)

> **Keep-alive tip:** Create a free [UptimeRobot](https://uptimerobot.com) monitor pointing at `https://your-app.onrender.com/ping` every 10 minutes to prevent cold-start delays on the free tier.

### Frontend → GitHub Pages

1. Go to your repo → **Settings → Pages → Source → main branch → / (root)**
2. Update the `API_BASE` constant in `index.html`:

```javascript
// In the <script> block at the bottom of index.html:
const API_BASE = (
  window.location.hostname === 'localhost' || ...
) ? 'http://localhost:8000'
  : 'https://your-movie-api.onrender.com'; // ← replace with your Render URL
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
    { "title": "Interstellar", "poster": "...", "rating": 8.1, "year": "2014", "genres": [...], "overview": "..." },
    ...
  ]
}
```

### `GET /health`

```json
{ "status": "ok", "movies_loaded": true, "model_loaded": true, "total_movies": 4806 }
```

### `GET /ping`

```json
{ "pong": true }
```

Full interactive documentation available at `/docs` (Swagger UI) when the server is running.

---

## ⚠️ Important — Model Files

`movie_list.pkl`, `similarity_quantized.pkl`, and `Dataset.zip` are **gitignored and not committed to this repository**.

They are generated locally by the Jupyter notebook. For Render deployment:

| Option | Description |
|:-------|:------------|
| **Render Disk** | Upload both `.pkl` files to persistent storage — recommended |
| **Docker** | Bundle files into a Docker image for fully reproducible deployment |
| **Re-generate at startup** | Add notebook execution to startup — slow (~2 min) but zero config |

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

Developed by **Nilotpal Dhar** &nbsp;·&nbsp; [Portfolio](https://nilotpal-dhar.vercel.app) &nbsp;·&nbsp; [LinkedIn](https://www.linkedin.com/in/nilotpal-dhar-24b304294/) &nbsp;·&nbsp; [Kaggle](https://www.kaggle.com/nilotpaldhar)
