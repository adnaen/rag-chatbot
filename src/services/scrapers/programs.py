from colorama import Fore
from src.core import logger
from src.services.scrapers.base import BaseScraper
from src.utils import clean_text


class ProgramScraper(BaseScraper):
    def __init__(self, url):
        super().__init__(category="program", sitemap_url=url)

    def scrape(self):
        """Fetches all links from sitemap and scrapes each page."""
        urls = self.fetch_sitemap_links()
        try:
            self.url_len = len(urls)
            for index, url in enumerate(urls, start=1):
                soup = self.fetch_content(url)
                program_content = soup.find(class_="program")
                if program_content:
                    logger.info(
                        f"{Fore.YELLOW}successfully scraped {index}/{len(urls)}{Fore.GREEN} {self.category} {Fore.RESET}{url}"
                    )
                    text = program_content.get_text(separator="\n", strip=True)

                    self.save_data(content=clean_text(text), index=index, url=url)

                else:
                    logger.error(
                        "there is no class such as 'program', scraping failed."
                    )

        except Exception as e:
            logger.exception(f"something went wrong as : {e}")
