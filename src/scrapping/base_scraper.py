import os
import json
from typing import Any
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from colorama import Fore

from src.utils import BasePath, logger


class BaseScraper:
    def __init__(self, category: str, sitemap_url: str) -> None:
        self.category = category
        self.sitemap_url = sitemap_url
        self.save_dir = BasePath.DATA_DIR / f"raw/{category}s"
        os.makedirs(self.save_dir, exist_ok=True)
        logger.info(
            f"Initialize BaseScraper with\ncategory: {self.category}\nsitemap url: {self.sitemap_url}\nsave dir: {self.save_dir}"
        )

    def fetch_sitemap_links(self) -> list[str]:
        logger.info(f"Fetching urls from : {self.sitemap_url}")
        try:
            response = requests.get(self.sitemap_url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "lxml-xml")
                each_pages = soup.find_all("url")
                urls = [each.find("loc").text for each in each_pages]
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
        """Fetches page content."""
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

    def save_data(self, content: Any, index: int) -> None:
        """Saves extracted text and metadata."""
        try:
            self.filename = (
                f"{self.category}_{index}_{datetime.now().strftime('%Y%m%d%H%M')}.txt"
            )
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
        keywords: list[str],
        summary: str,
        url: str,
        status: bool = True,
        err_msg: str | None = None,
    ) -> None:
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
            "keywords": keywords,
            "summary": summary,
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

    def scrape(self):
        """This method should be implemented by child classes."""
        raise NotImplementedError
