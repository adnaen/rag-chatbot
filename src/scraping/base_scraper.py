import os
import json
from typing import Any
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from colorama import Fore

from src.utils import BasePath, logger


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
        self.save_dir = BasePath.DATA_DIR / f"raw/{category}s"
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
        return match.group()

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
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            logger.info(f"{Fore.YELLOW}file saved in{Fore.RESET} {file_path}")
        except Exception as e:
            logger.exception(f"something went wrong as : {e}")

    def save_metadata(
        self,
        id: int,
        title: str,
        word_count: int,
        num_paragraphs: int,
        url: str,
        status: bool = True,
        err_msg: str | None = None,
    ) -> None:
        """
        Args:
            id (int) : index like.
            title (str) : title of the stored file.
            word_count (int)
            num_paragraphs (int)
            url (URL_LIKE) : fetched domain.
            status (bool) : either scrap success or not.
            err_msg (str) | None : if status is false, what is the reason for it.

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
            "date_scraped": str(datetime.now()),
            "word_count": word_count,
            "num_paragraphs": num_paragraphs,
            "scraped_status": "success" if status else "failed",
            "error_message": err_msg,
        }
        metadata = []
        if os.path.exists(metadata_file):
            with open(metadata_file, "r", encoding="utf-8") as f:
                metadata = json.load(f)

        metadata.append(data)

        with open(metadata_file, "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=4)

    def save_global_metadata(self, data: dict) -> None:
        """Save global metadata for the category.
        Args:
            data (dict) : metadata to be stored.

        Returns:
            None
        """
        metadata_file = BasePath.DATA_DIR / "raw/metadata.json"
        metadata = []
        if os.path.exists(metadata_file):
            with open(metadata_file, "r", encoding="utf-8") as f:
                metadata = json.load(f)

        data.update({"stored_path": str(self.save_dir)})
        metadata.append(data)

        with open(metadata_file, "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=4)

    def scrape(self):
        """This method should be implemented by child classes."""
        raise NotImplementedError
