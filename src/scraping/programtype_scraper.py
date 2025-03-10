from colorama import Fore
from src.scraping import BaseScraper, preprocess_text
from src.utils import logger


class ProgramTypeScraper(BaseScraper):
    def __init__(self, url):
        super().__init__(category="programtype", sitemap_url=url)

    def scrape(self):
        """Fetches all links from sitemap and scrapes each page."""
        urls = self.fetch_sitemap_links()
        try:
            self.url_len = len(urls)
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

                    self.save_data(content=preprocess_text(text), index=index, url=url)
                    self.save_metadata(
                        id=index,
                        url=url,
                        word_count=word_count,
                        num_paragraphs=num_paragraphs,
                        title=self.get_page_name(url),
                    )

                else:
                    logger.error(
                        "there is no class such as 'program page', scraping failed."
                    )

            global_info = {
                "total_pages": str(self.url_len),
                "category": str(self.category),
            }
            self.save_global_metadata(data=global_info)
        except Exception as e:
            logger.exception(f"something went wrong as : {e}")
