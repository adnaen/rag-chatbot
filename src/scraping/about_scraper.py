from colorama import Fore
from src.scraping import BaseScraper, preprocess_text
from src.utils import logger


class AboutScraper(BaseScraper):
    def __init__(self, url):
        super().__init__(category="about", sitemap_url=url)

    def scrape(self):
        """Fetches all links from sitemap and scrapes each page."""
        urls = self.fetch_sitemap_links()
        try:
            for index, url in enumerate(urls, start=1):
                soup = self.fetch_content(url)
                if soup is None:
                    logger.error(f"Failed to fetch content from {url}. Skipping...")
                    continue

                about_content = soup.find(id="pageWrapper")
                if about_content:
                    logger.info(
                        f"{Fore.YELLOW}Successfully scraped {index}/{len(urls)}{Fore.GREEN} {self.category} {Fore.RESET}{url}"
                    )
                    text = about_content.get_text(separator="\n", strip=True)
                    word_count = len(text.split())
                    num_paragraphs = text.count("\n")

                    self.save_data(content=preprocess_text(text), index=index)
                    self.save_metadata(
                        id=index,
                        url=url,
                        word_count=word_count,
                        num_paragraphs=num_paragraphs,
                        title="about page",
                        summary="summary of the about page content",
                        keywords=["about", "company", "information"],
                    )
                else:
                    logger.error(
                        f"No content found in {url}. Check the HTML structure."
                    )
        except Exception as e:
            logger.exception(f"Something went wrong: {e}")
