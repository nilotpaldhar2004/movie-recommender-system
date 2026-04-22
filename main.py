import os
import pickle
import logging
import time

import joblib
import numpy as np
import requests
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from contextlib import asynccontextmanager


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("movie-recommender")

TMDB_API_KEY  = os.getenv("TMDB_API_KEY", "8265bd1679663a7ea12ac168da84d2e8")
TMDB_BASE     = "https://api.themoviedb.org/3"
TMDB_IMG_BASE = "https://image.tmdb.org/t/p/w500"
PORT      = int(os.getenv("PORT", 7860))


ml = {}
@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Loading movie metadata …")
    try:
        ml["movies"] = pickle.load(open("movie_list.pkl", "rb"))
        logger.info("Loaded %d movies.", len(ml["movies"]))
    except FileNotFoundError:
        logger.error("movie_list.pkl not found.")
        ml["movies"] = None

    logger.info("Loading similarity matrix …")
    try:
        raw = joblib.load("similarity_quantized.pkl").astype(np.float32) / 255
        ml["similarity"] = raw
        logger.info("Similarity matrix loaded: %s", raw.shape)
    except FileNotFoundError:
        logger.error("similarity_quantized.pkl not found.")
        ml["similarity"] = None

    yield
    ml.clear()
    logger.info("Shutting down — resources released.")

app = FastAPI(
    title="Movie Recommender API",
    description="NLP content-based movie recommendation engine using cosine similarity on TMDB data.",
    version="2.0.0",
    lifespan=lifespan,
    docs_url="/docs",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def timing_middleware(request, call_next):
    t0       = time.perf_counter()
    response = await call_next(request)
    response.headers["X-Process-Time-Ms"] = f"{(time.perf_counter()-t0)*1000:.1f}"
    return response

def fetch_movie_details(movie_id: int) -> dict:
    try:
        url  = f"{TMDB_BASE}/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
        data = requests.get(url, timeout=8).json()
        poster_path  = data.get("poster_path")
        genres       = [g["name"] for g in data.get("genres", [])][:3]
        return {
            "poster":   f"{TMDB_IMG_BASE}{poster_path}" if poster_path else "",
            "rating":   round(data.get("vote_average", 0), 1),
            "year":     (data.get("release_date") or "")[:4],
            "overview": data.get("overview", ""),
            "genres":   genres,
        }
    except Exception as exc:
        logger.warning("TMDB fetch failed for movie_id=%s: %s", movie_id, exc)
        return {"poster": "", "rating": 0, "year": "", "overview": "", "genres": []}


@app.get("/", include_in_schema=False)
async def serve_frontend():
    if os.path.exists("index.html"):
        return FileResponse("index.html")
    return {"message": "Movie Recommender API v2.0.0 — GET /docs for API reference"}


@app.get("/ping", include_in_schema=False)
async def ping():
    """Keep-alive endpoint — point UptimeRobot here every 10 minutes."""
    return {"pong": True}


@app.get("/health", tags=["System"])
async def health():
    ready = ml.get("movies") is not None and ml.get("similarity") is not None
    return JSONResponse(
        status_code=200 if ready else 503,
        content={
            "status":         "ok" if ready else "degraded",
            "movies_loaded":  ml.get("movies") is not None,
            "model_loaded":   ml.get("similarity") is not None,
            "total_movies":   len(ml["movies"]) if ml.get("movies") is not None else 0,
        },
    )


@app.get("/movies", tags=["Data"])
async def list_movies():

    if ml.get("movies") is None:
        raise HTTPException(503, "Model not ready.")
    titles = ml["movies"]["title"].tolist()
    return {"count": len(titles), "movies": titles}


@app.get("/recommend", tags=["Inference"])
async def recommend(movie: str, n: int = 5):

    movies_df  = ml.get("movies")
    similarity = ml.get("similarity")

    if movies_df is None or similarity is None:
        raise HTTPException(503, "Model not ready. Check /health.")

    n = max(1, min(n, 10))

    matches = movies_df[movies_df["title"].str.lower() == movie.lower()]
    if matches.empty:
        raise HTTPException(404, f"Movie '{movie}' not found. Use /movies to browse titles.")

    idx       = matches.index[0]
    distances = sorted(enumerate(similarity[idx]), key=lambda x: x[1], reverse=True)


    selected_id      = int(movies_df.iloc[idx].id)
    selected_details = fetch_movie_details(selected_id)
    selected_details["title"] = movies_df.iloc[idx].title

    recommendations = []
    for i, _ in distances[1 : n + 1]:
        movie_id = int(movies_df.iloc[i].id)
        details  = fetch_movie_details(movie_id)
        details["title"] = movies_df.iloc[i].title
        recommendations.append(details)

    logger.info("Recommended %d movies for '%s'", n, movie)
    return {
        "query":           movie,
        "selected":        selected_details,
        "recommendations": recommendations,
    }

if __name__ == "__main__":
    import uvicorn
    logger.info("Starting Movie Recommender API on port %d", PORT)
    uvicorn.run("main:app", host="0.0.0.0", port=PORT, reload=False)