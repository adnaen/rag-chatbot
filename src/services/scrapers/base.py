import os
import requests
from typing import Any, List
from colorama import Fore
from bs4 import BeautifulSoup
from src.core import logger, settings


class BaseScraper:
    """
    BaseScraper class which contain all steps to be perform scraping
    """

    def __init__(self, category: str, sitemap_url: str) -> None:
        """
        Initializing BaseScraper class.

        Args:
            category (str) : category to be scrap
            sitemap_url (URL_LIKE) : sitemap index link
        """
        self.category = category
        self.sitemap_url = sitemap_url
        self.save_dir = settings.DATA_DIR / f"raw/{category}s"
        os.makedirs(self.save_dir, exist_ok=True)
        logger.info(
            f"Initialize BaseScraper with\ncategory: {self.category}\nsitemap url: {self.sitemap_url}\nsave dir: {self.save_dir}"
        )

    def fetch_sitemap_links(self, exclude: List[str] | None = None) -> List[str]:
        """
        fetch all child pages url from the sitemap.

        Args:
            exclude (List[str]) : List of urls to exclude from the fetched urls.

        Returns:
            List[str] : List of urls
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
            with open(file_path, "w") as file:
                file.write(content)

            logger.info(f"{Fore.YELLOW}file saved in{Fore.RESET} {file_path}")
        except Exception as e:
            logger.exception(f"something went wrong as : {e}")

    def scrape(self):
        """This method should be implemented by child classes."""
        raise NotImplementedError
