from typing import List
from pathlib import Path
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    # paths
    PROJECT_DIR: Path = Path(__file__).resolve().parents[2]
    ARTIFACTS_DIR: Path = PROJECT_DIR / "artifacts"
    DATA_DIR: Path = ARTIFACTS_DIR / "data" / "raw"
    MODEL_DIR: Path = ARTIFACTS_DIR / "models"
    CHROMA_DIR: Path = ARTIFACTS_DIR / "chroma"

    ABOUT_DATA_DIR: Path = DATA_DIR / "abouts"
    PROGRAM_TYPE_DATA_DIR: Path = DATA_DIR / "programtypes"
    PROGRAM_DATA_DIR: Path = DATA_DIR / "programs"
    BLOGS_DATA_DIR: Path = DATA_DIR / "blogs"

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

    CHUNK_SIZE: int = 2000
    CHUNK_OVERLAP: int = 200

    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"
    CHROMA_COLLECTION: str = "scraped_data"

    LLM: str = "tinyllama_1_1b_chat_v1_0_gguf"
    LLM_TOP_P: float = 0.96
    LLM_TOP_K: int = 40
    LLM_TEMPERATURE: float = 0.8
    MAX_TOKENS: int = 2042
    N_THREADS: int = 3  # total core - 1
    N_CTX: int = 2042


settings = Settings()
