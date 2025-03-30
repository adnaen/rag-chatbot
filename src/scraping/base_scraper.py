import os
from typing import Any
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from colorama import Fore

from src.config import logger
from src.config import paths
from src.utils.file_utils import _save_file, _load_json, _dump_json


class BaseScraper:
    """
    BaseScraper class which contain all steps to be perform while scraping
    """

    def __init__(self, category: str, sitemap_url: str) -> None:
        """
        Initializing BaseScraper class.
        Args:
            category (str) : category to be scrap, !!it should be singular!!.
            sitemap_url (URL_LIKE) : sitemap index link to the category
        """
        self.category = category
        self.sitemap_url = sitemap_url
        self.save_dir = paths.DATA_DIR / f"raw/{category}s"
        os.makedirs(self.save_dir, exist_ok=True)
        logger.info(
            f"Initialize BaseScraper with\ncategory: {self.category}\nsitemap url: {self.sitemap_url}\nsave dir: {self.save_dir}"
        )

    def fetch_sitemap_links(self, exclude: list[str] | None = None) -> list[str]:
        """
        fetch all child pages url from the sitemap.

        Args:
            exclude (list[str]) : list of urls to exclude from the fetched urls.

        Returns:
            list[str] : list of urls
        """
        logger.info(f"Fetching urls from : {self.sitemap_url}")
        try:
            response = requests.get(self.sitemap_url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "lxml-xml")
                each_pages = soup.find_all("url")
                urls = [each.find("loc").text for each in each_pages]
                if exclude:
                    logger.info(f"excluding urls : {exclude}")
                    urls = [url for url in urls if url not in exclude]

                logger.info(f"fetched url count : {len(urls)}")
                logger.info(
                    f"successfully fetched all urls from {self.category} sitemap"
                )
                return urls
            logger.error(
                f"cannot fetch {self.sitemap_url}, status code : {response.status_code}"
            )
            return []
        except Exception as e:
            logger.exception(f"something went wrong as : {e}")
            return []

    def fetch_content(self, url: str) -> BeautifulSoup | None:
        """Fetches page content.
        Args:
            url (URL_LIKE) : url to scrap the page text

        Returns:
            BeautifulSoup | None : if success all text in the url, else None
        """
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return BeautifulSoup(response.text, "html.parser")
            else:
                logger.error(
                    f"cannot fetch {url}, status code : {response.status_code}"
                )
                return None
        except Exception as e:
            logger.exception(f"something went wrong as : {e}")
            return None

    def get_page_name(self, url: str) -> str:
        import re

        pattern = r"[^/]+(?=\/?$)"
        match = re.search(pattern, url)
        result = match.group()
        return result.replace("_", " ").title()

    def save_data(self, content: Any, index: int, url: str) -> None:
        """Saves extracted text and metadata.
        Args:
            content (any) : content to be stored in .txt file.
            index (int) : current index number. e.g. 98/190

        Returns:
            None
        """
        try:
            self.filename = f"{self.get_page_name(url)}.txt"
            file_path = self.save_dir / self.filename
            _save_file(content=content, path=file_path)
            logger.info(f"{Fore.YELLOW}file saved in{Fore.RESET} {file_path}")
        except Exception as e:
            logger.exception(f"something went wrong as : {e}")

    def save_metadata(
        self,
        id: int,
        title: str,
        url: str,
    ) -> None:
        """
        Args:
            id (int) : index like.
            title (str) : title of the stored file.
            url (URL_LIKE) : fetched domain.

        Returns:
            None
        """
        metadata_file = self.save_dir / "metadata.json"
        data = {
            "id": id,
            "url": url,
            "file_name": self.filename,
            "title": title,
            "processed_path": str(self.save_dir / self.filename),
        }
        metadata = []
        if os.path.exists(metadata_file):
            metadata = _load_json(path=metadata_file)
        metadata.append(data)

        _dump_json(content=metadata, path=metadata_file)

    def save_global_metadata(self, data: dict) -> None:
        """Save global metadata for the category.
        Args:
            data (dict) : metadata to be stored.

        Returns:
            None
        """
        metadata_file = paths.DATA_DIR / "raw/metadata.json"
        metadata = []
        if os.path.exists(metadata_file):
            metadata = _load_json(path=metadata_file)

        data.update({"stored_path": str(self.save_dir)})
        metadata.append(data)

        _dump_json(content=metadata, path=metadata_file)

    def scrape(self):
        """This method should be implemented by child classes."""
        raise NotImplementedError
