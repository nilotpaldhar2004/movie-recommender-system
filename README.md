---
title: Movie Recommender AI
emoji: 🎬
colorFrom: red
colorTo: gray
sdk: docker
app_file: main.py
pinned: false
---

# 🎬 CineMatch — NLP-Powered Movie Recommender

<div align="center">

[![Live Demo](https://img.shields.io/badge/Demo-Live%20Site-brightgreen?style=for-the-badge&logo=github)](https://nilotpaldhar2004.github.io/movie-recommender-system/)
[![HuggingFace](https://img.shields.io/badge/Backend-HuggingFace%20Spaces-orange?style=for-the-badge&logo=huggingface)](https://huggingface.co/spaces/nilotpaldhar2004/movie-recommender-ai)
[![FastAPI](https://img.shields.io/badge/API-FastAPI-009688?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Dataset](https://img.shields.io/badge/Dataset-TMDB%205000-orange?style=for-the-badge)](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)

</div>

A content-based movie recommendation engine built with NLP and cosine similarity. Type any movie title — the system returns 5 films with matching storylines, genres, cast, and cinematic DNA. Deployed as a **Dockerized FastAPI backend on HuggingFace Spaces** with a standalone frontend on GitHub Pages.

🚀 **[Try the Live Demo](https://nilotpaldhar2004.github.io/movie-recommender-system/)**  
🤗 **[HuggingFace Space](https://huggingface.co/spaces/nilotpaldhar2004/movie-recommender-ai)**

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

## 🌐 Deployment

Migrated from Render to **HuggingFace Spaces** for persistent uptime, no cold-start delays, and better ML project visibility.

| Component | Platform | URL |
|---|---|---|
| Full App (API + UI) | HuggingFace Spaces (Docker) | `https://huggingface.co/spaces/nilotpaldhar2004/movie-recommender-ai` |
| Frontend Mirror | GitHub Pages | `https://nilotpaldhar2004.github.io/movie-recommender-system/` |

- **Infrastructure:** Docker (Python 3.10-slim)
- **CI/CD:** GitHub Actions automatically syncs every push from `main` to the HuggingFace Space, triggering an automated rebuild.

> **Why moved from Render?** HuggingFace Spaces has no cold-start delays on free tier, persistent storage for model files, and is purpose-built for ML apps.

---

## ✨ Features

- **Instant autocomplete** — starts from first character, sorted starts-with first then contains, with keyboard navigation
- **5,000-movie corpus** — trained on the TMDB 5000 Movie Dataset from Kaggle
- **Live TMDB metadata** — posters, ratings, release year, genres, and overviews fetched in real time
- **Selected film card** — shows full details of your searched movie alongside recommendations
- **Hover overlay** — movie overview slides in on poster hover
- **Cinematic UI** — deep indigo-violet gradient background with electric cyan accents
- **Responsive** — 2 columns (mobile) → 3–4 columns (tablet) → 5 columns (desktop)

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **NLP / ML** | Scikit-Learn (CountVectorizer, cosine_similarity) |
| **Backend API** | FastAPI, Uvicorn, Requests |
| **Frontend** | HTML5, CSS3, Vanilla JavaScript |
| **Deployment/DevOps** | Docker, HuggingFace Spaces, GitHub Actions |
| **Training** | Jupyter Notebook (Kaggle) |
| **Data** | TMDB 5000 Movie Dataset |
| **External API** | TMDB (The Movie Database) |

---

## 📂 Project Structure

```
movie-recommender-system/
│
├── main.py                          # FastAPI backend
├── index.html                       # Frontend web interface
├── Dockerfile                       # HuggingFace Spaces deployment
├── requirements.txt                 # Python dependencies (pinned)
├── LICENSE                          # MIT License
├── README.md                        # This file
│
├── .github/workflows/
│   └── deploy.yml                   # Auto-deploy to HF Spaces on push
│
└── (gitignored — not committed)
    ├── movie_list.pkl               # Movie metadata DataFrame (~5MB)
    ├── similarity_quantized.pkl     # Quantized cosine similarity matrix (~23MB)
    └── Dataset.zip                  # Raw TMDB dataset (download from Kaggle)
```

---

## 🚀 Getting Started Locally

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

```
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata
```

Place downloaded files in the project root.

### 4. Generate model files

Open and run all cells in `Movie Recommender System.ipynb` — generates `movie_list.pkl` and `similarity_quantized.pkl`.

### 5. Start the server

```bash
uvicorn main:app --reload --port 8000
```

Open `http://localhost:8000` — FastAPI serves `index.html` directly.

---

## 🐳 Deploy to HuggingFace Spaces

### Manual upload

1. Go to [huggingface.co/spaces](https://huggingface.co/spaces) → **Create new Space**
2. Select **Docker** as SDK
3. Upload: `main.py`, `index.html`, `requirements.txt`, `Dockerfile`, `movie_list.pkl`, `similarity_quantized.pkl`
4. Space auto-builds and gives a public URL

### Auto-deploy via GitHub Actions

Every push to `main` automatically deploys to HF Spaces.

```yaml
# .github/workflows/deploy.yml
name: Deploy to HuggingFace Spaces
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Push to HuggingFace Space
        env:
          HF_TOKEN: ${{ secrets.HF_TOKEN }}
        run: |
          git config --global user.email "dharnilotpal31@gmail.com"
          git config --global user.name "nilotpaldhar2004"
          git clone https://nilotpaldhar2004:${HF_TOKEN}@huggingface.co/spaces/nilotpaldhar2004/movie-recommender-ai hf_space
          cp main.py index.html requirements.txt Dockerfile hf_space/
          cd hf_space
          git add .
          git diff --cached --quiet || git commit -m "Auto deploy from GitHub"
          git remote set-url origin https://nilotpaldhar2004:${HF_TOKEN}@huggingface.co/spaces/nilotpaldhar2004/movie-recommender-ai
          git push origin main
```

---

## 📡 API Reference

### `GET /movies`

Returns all movie titles for the autocomplete dropdown.

```json
{ "count": 4806, "movies": ["Avatar", "Inception", "The Dark Knight", "..."] }
```

### `GET /recommend?movie=Inception&n=5`

Returns top-N content-based recommendations.

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
    { "title": "Interstellar", "poster": "...", "rating": 8.1, "year": "2014" },
    ...
  ]
}
```

### `GET /health`

```json
{ "status": "ok", "movies_loaded": true, "model_loaded": true, "total_movies": 4806 }
```

Full interactive docs at `/docs` (Swagger UI) when server is running.

---

## ⚠️ Model Files

`movie_list.pkl`, `similarity_quantized.pkl`, and `Dataset.zip` are **gitignored — not committed to this repo.**

Generated locally by the Jupyter notebook. Upload them directly to the HuggingFace Space via the Files tab or include in Docker image.

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

## 👤 Author

**Nilotpal Dhar**

[![GitHub](https://img.shields.io/badge/GitHub-nilotpaldhar2004-black?style=flat&logo=github)](https://github.com/nilotpaldhar2004)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-nilotpaldhar2004-orange?style=flat)](https://huggingface.co/nilotpaldhar2004)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-nilotpal--dhar-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/nilotpal-dhar-24b304294/)
[![Kaggle](https://img.shields.io/badge/Kaggle-nilotpaldhar-20beff?style=flat&logo=kaggle)](https://www.kaggle.com/nilotpaldhar)

---

<div align="center">
  <sub>Built with Python, FastAPI, and Scikit-Learn · Deployed on HuggingFace Spaces via Docker + GitHub Actions CI/CD</sub>
</div>
