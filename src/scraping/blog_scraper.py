from colorama import Fore

from src.scraping import BaseScraper
from src.utils.data_utils import _preprocess_text
from src.config import logger


class BlogScraper(BaseScraper):
    def __init__(self, url):
        super().__init__(category="blog", sitemap_url=url)

    def scrape(self):
        """Fetches all links from sitemap and scrapes each page."""
        exclude_urls = [
            "https://empirecollege.in/blog/%e0%b4%85%e0%b4%ae%e0%b4%bf%e0%b4%a4-%e0%b4%b5%e0%b4%a3%e0%b5%8d%e0%b4%a3%e0%b4%82-%e0%b4%8e%e0%b4%a8%e0%b5%8d%e0%b4%a4%e0%b5%81%e0%b4%95%e0%b5%8a%e0%b4%a3%e0%b5%8d%e0%b4%9f%e0%b5%8d-%e0%b4%8e/",
        ]
        urls = self.fetch_sitemap_links(exclude=exclude_urls)
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
                    word_count = len(text.split())
                    num_paragraphs = text.count("\n")

                    self.save_data(content=_preprocess_text(text), index=index, url=url)
                    self.save_metadata(
                        id=index,
                        url=url,
                        title=self.get_page_name(url),
                    )

                else:
                    logger.error(
                        "there is no class such as 'contentWrap', scraping failed."
                    )

            global_info = {
                "total_pages": self.url_len,
                "category": self.category,
            }
            self.save_global_metadata(data=global_info)

        except Exception as e:
            logger.exception(f"something went wrong as : {e}")
