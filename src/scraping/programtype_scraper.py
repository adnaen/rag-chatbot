from colorama import Fore
from src.scraping import BaseScraper
from src.utils import logger

class ProgramTypeScraper(BaseScraper):
    def __init__(self, url):
        super().__init__(category="programtype", sitemap_url=url)

    def scrape(self):
        """Fetches all links from sitemap and scrapes each page."""
        urls = self.fetch_sitemap_links()
        try:
            for index, url in enumerate(urls, start=1):
                soup = self.fetch_content(url)
                programtype_content = soup.find(class_="programPage")
                if programtype_content:
                    logger.info(
                        f"{Fore.YELLOW}successfully scraped {index}/{len(urls)}{Fore.GREEN} {self.category} {Fore.RESET}{url}"
                    )
                    text = programtype_content.get_text(separator="\n", strip=True)
                    word_count = len(text.split())
                    num_paragraphs = text.count("\n")

                    self.save_data(content=text, index=index)
                    self.save_metadata(
                        id=index,
                        url=url,
                        word_count=word_count,
                        num_paragraphs=num_paragraphs,
                        title="none",
                        summary="none",
                        keywords=["none", "none"],
                    )

                else:
                    logger.error(
                        "there is no class such as 'program page', scraping failed."
                    )
        except Exception as e:
            logger.exception(f"something went wrong as : {e}")
