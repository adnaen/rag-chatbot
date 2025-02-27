from pathlib import Path
from dataclasses import dataclass


@dataclass
class BasePath:
    """
    project level constant variables and paths
    """

    PROJECT_DIR: Path = Path(__file__).resolve().parents[2]
    ARTIFACTS_DIR: Path = PROJECT_DIR / "artifacts"
    DATA_DIR: Path = ARTIFACTS_DIR / "data"

    # web urls
    BASE_URL: str = "https://empirecollege.in/"
    SITEMAP_INDEX_URL: str = "https://empirecollege.in/sitemap_index.xml"
    BLOG_SITEMAP_URL: str = "https://empirecollege.in/post-sitemap.xml"
    PROGRAMTYPE_SITEMAP_URL: str = "https://empirecollege.in/program-type-sitemap.xml"
