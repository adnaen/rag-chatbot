from typing import List
from pathlib import Path
from dataclasses import dataclass


@dataclass
class Settings:

    # paths
    PROJECT_DIR: Path = Path(__file__).resolve().parents[2]
    ARTIFACTS_DIR: Path = PROJECT_DIR / "artifacts"
    DATA_DIR: Path = ARTIFACTS_DIR / "data"
    CONFIG_DIR: Path = PROJECT_DIR / "src" / "config"
    DB_DIR: Path = ARTIFACTS_DIR / "chroma_db"
    MODEL_DIR: Path = PROJECT_DIR / "models"

    # scrapping URLs
    BASE_SITE_URL: str = "https://empirecollege.in"
    SITEMAP_INDEX_URL: str = f"{BASE_SITE_URL}/sitemap_index.xml"
    BLOG_SITEMAP_URL: str = f"{BASE_SITE_URL}/post-sitemap.xml"
    PROGRAM_TYPE_SITEMAP_URL: str = f"{BASE_SITE_URL}/program-type-sitemap.xml"
    ABOUT_SITEMAP_URL: str = f"{BASE_SITE_URL}/page-sitemap.xml"
    PROGRAM_SITEMAP_URL: str = f"{BASE_SITE_URL}/program-sitemap.xml"
    EXCLUDE_URLS: List[str] = [
        f"{BASE_SITE_URL}/newsletter/",
        f"{BASE_SITE_URL}/blogs/",
        f"{BASE_SITE_URL}/program/",
        f"{BASE_SITE_URL}/gallery/",
        f"{BASE_SITE_URL}/blog/%e0%b4%85%e0%b4%ae%e0%b4%bf%e0%b4%a4-%e0%b4%b5%e0%b4%a3%e0%b5%8d%e0%b4%a3%e0%b4%82-%e0%b4%8e%e0%b4%a8%e0%b5%8d%e0%b4%a4%e0%b5%81%e0%b4%95%e0%b5%8a%e0%b4%a3%e0%b5%8d%e0%b4%9f%e0%b5%8d-%e0%b4%8e/",
    ]

    CHUNK_SIZE: int = 1500
    CHUNK_WRAP_SIZE: int = 200
