from colorama import Fore
from src.core import logger, Settings
from src.services.scrapers.base import BaseScraper
from src.utils import clean_text


class AboutScraper(BaseScraper):
    def __init__(self, url):
        super().__init__(category="about", sitemap_url=url)

    def scrape(self):
        """Fetches all links from sitemap and scrapes each page."""
        urls = self.fetch_sitemap_links(exclude=Settings.EXCLUDE_URLS)
        try:
            self.url_len = len(urls)
            for index, url in enumerate(urls, start=1):
                soup = self.fetch_content(url)
                if soup is None:
                    logger.error(f"Failed to fetch content from {url}. Skipping...")
                    continue

                about_content = soup.find(id="pageWrapper")
                if about_content:
                    logger.info(
                        f"{Fore.YELLOW}Successfully scraped {index}/{self.url_len}{Fore.GREEN} {self.category} {Fore.RESET}{url}"
                    )
                    text = about_content.get_text(separator="\n", strip=True)

                    self.save_data(content=clean_text(text), index=index, url=url)
                else:
                    logger.error(
                        f"No content found in {url}. Check the HTML structure."
                    )
        except Exception as e:
            logger.exception(f"Something went wrong: {e}")
