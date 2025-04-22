from colorama import Fore
from src.scraping import BaseScraper
from src.utils.data_utils import _preprocess_text
from src.config import logger


class AboutScraper(BaseScraper):
    def __init__(self, url):
        super().__init__(category="about", sitemap_url=url)

    def scrape(self):
        """Fetches all links from sitemap and scrapes each page."""
        exclude_urls = [
            "https://empirecollege.in/newsletter/",
            "https://empirecollege.in/blogs/",
            "https://empirecollege.in/program/",
            "https://empirecollege.in/gallery/",
        ]
        urls = self.fetch_sitemap_links(exclude=exclude_urls)
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

                    self.save_data(content=_preprocess_text(text), index=index, url=url)
                    self.save_metadata(
                        id=index,
                        url=url,
                        title=self.get_page_name(url),
                    )
                else:
                    logger.error(
                        f"No content found in {url}. Check the HTML structure."
                    )
            global_info = {
                "total_pages": self.url_len,
                "category": self.category,
            }
            self.save_global_metadata(data=global_info)
        except Exception as e:
            logger.exception(f"Something went wrong: {e}")
