"""
Supplementary data fetchers for the ML repo.
These are enhanced fetchers that integrate APIs from the other agent's build:
- Kaggle API for C-MAPSS (fallback to direct download)
- Reddit/PRAW for live text classification
- OpenWeatherMap for weather-enriched bike demand
- Citi Bike GBFS for real-time station data
"""

from __future__ import annotations

import io, os, zipfile
from pathlib import Path
from typing import Any, List, Optional
import requests
from dotenv import load_dotenv

# ──────────────────────────────────────────────────────────
# Kaggle API — NASA C-MAPSS fallback
# ──────────────────────────────────────────────────────────

def download_cmapss_kaggle(data_dir: str | Path, dataset_slug: Optional[str] = None) -> Path:
    """
    Download NASA C-MAPSS via Kaggle API.
    Fallback if direct NASA download is unavailable.
    
    Requires KAGGLE_USERNAME and KAGGLE_KEY env vars.
    Default dataset slug: 'behrad3d/nasa-cmaps'
    """
    load_dotenv()
    slug = dataset_slug or os.getenv("CMAPSS_DATASET_SLUG", "behrad3d/nasa-cmaps")
    if not (os.getenv("KAGGLE_USERNAME") and os.getenv("KAGGLE_KEY")):
        raise ValueError("Set KAGGLE_USERNAME and KAGGLE_KEY before using Kaggle download.")
    try:
        from kaggle.api.kaggle_api_extended import KaggleApi
    except ImportError as exc:
        raise ImportError("Install kaggle to use this downloader: pip install kaggle") from exc
    out = Path(data_dir)
    out.mkdir(parents=True, exist_ok=True)
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(slug, path=str(out), unzip=True)
    return out


# ──────────────────────────────────────────────────────────
# Reddit/PRAW — Live text data for NLP
# ──────────────────────────────────────────────────────────

def fetch_reddit_posts(subreddit: str, limit: int = 25) -> List[str]:
    """
    Fetch live posts from Reddit using PRAW.
    
    Requires REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT env vars.
    Returns list of post texts (title + selftext).
    """
    load_dotenv()
    required = ["REDDIT_CLIENT_ID", "REDDIT_CLIENT_SECRET", "REDDIT_USER_AGENT"]
    if not all(os.getenv(k) for k in required):
        raise ValueError(f"Set {', '.join(required)} to use Reddit fetcher.")
    try:
        import praw
    except ImportError as exc:
        raise ImportError("Install praw to use Reddit fetcher: pip install praw") from exc
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT"),
    )
    posts = []
    for submission in reddit.subreddit(subreddit).hot(limit=limit):
        text = (submission.title or "") + "\n" + (submission.selftext or "")
        posts.append(text)
    return posts


# ──────────────────────────────────────────────────────────
# OpenWeatherMap — Weather enrichment for bike demand
# ──────────────────────────────────────────────────────────

def fetch_weather(city: str | None = None, api_key: str | None = None) -> dict[str, Any]:
    """
    Fetch current weather from OpenWeatherMap API.
    
    Requires OPENWEATHER_API_KEY env var.
    Returns JSON dict with temperature, humidity, weather condition, etc.
    """
    load_dotenv()
    key = api_key or os.getenv("OPENWEATHER_API_KEY")
    if not key:
        raise ValueError("Set OPENWEATHER_API_KEY or pass api_key.")
    q = city or os.getenv("OPENWEATHER_CITY", "Washington,US")
    r = requests.get(
        "https://api.openweathermap.org/data/2.5/weather",
        params={"q": q, "appid": key, "units": "metric"},
        timeout=10
    )
    r.raise_for_status()
    return r.json()


# ──────────────────────────────────────────────────────────
# Citi Bike GBFS — Real-time station status
# ──────────────────────────────────────────────────────────

def fetch_citibike_station_status() -> dict[str, Any]:
    """
    Fetch real-time Citi Bike station status via GBFS (General Bikeshare Feed Specification).
    No API key required.
    Returns JSON dict with station availability, bike counts, etc.
    """
    CITIBIKE_STATION_STATUS = "https://gbfs.citibikenyc.com/gbfs/en/station_status.json"
    r = requests.get(CITIBIKE_STATION_STATUS, timeout=10)
    r.raise_for_status()
    return r.json()


# ──────────────────────────────────────────────────────────
# UCI Bike Sharing — Direct download (alternative to Kaggle)
# ──────────────────────────────────────────────────────────

def download_bike_data(data_dir: str | Path, url: str = "https://archive.ics.uci.edu/ml/machine-learning-databases/00275/Bike-Sharing-Dataset.zip") -> Path:
    """
    Download UCI Bike Sharing dataset directly.
    No API key required.
    """
    out = Path(data_dir)
    out.mkdir(parents=True, exist_ok=True)
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    with zipfile.ZipFile(io.BytesIO(r.content)) as zf:
        zf.extractall(out)
    return out


if __name__ == "__main__":
    # Quick test: download bike data
    print("Testing UCI Bike data download...")
    path = download_bike_data("/tmp/bike_test")
    print(f"Downloaded to: {path}")
    print(f"Files: {list(path.glob('*'))}")
