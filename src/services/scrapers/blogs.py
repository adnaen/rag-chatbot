from colorama import Fore
from src.core import logger, Settings
from src.utils import clean_text
from src.services.scrapers.base import BaseScraper


class BlogScraper(BaseScraper):
    def __init__(self, url):
        super().__init__(category="blog", sitemap_url=url)

    def scrape(self):
        """Fetches all links from sitemap and scrapes each page."""
        urls = self.fetch_sitemap_links(exclude=Settings.EXCLUDE_URLS)
        try:
            self.url_len = len(urls)
            for index, url in enumerate(urls, start=1):
                soup = self.fetch_content(url)
                blog_content = soup.find(class_="contentWrap")
                if blog_content:
                    logger.info(
                        f"{Fore.YELLOW}successfully scraped {index}/{len(urls)}{Fore.GREEN} {self.category} {Fore.RESET}{url}"
                    )
                    text = blog_content.get_text(separator="\n", strip=True)

                    self.save_data(content=clean_text(text), index=index, url=url)

                else:
                    logger.error(
                        "there is no class such as 'contentWrap', scraping failed."
                    )

        except Exception as e:
            logger.exception(f"something went wrong as : {e}")
