from colorama import Fore

from src.scraping.blog_scraper import BlogScraper
from src.scraping.programtype_scraper import ProgramTypeScraper
from src.scraping.about_scraper import AboutScraper
from src.utils import BasePath, logger

def run_scraper() -> None:
    """
    Run all the scrapers.

    Args:
        None

    Returns:
        None
    """
    SCRAPERS = (BlogScraper(BasePath.BLOG_SITEMAP_URL),ProgramTypeScraper(BasePath.PROGRAMTYPE_SITEMAP_URL),AboutScraper(BasePath.ABOUT_SITEMAP_URL))   

    for scraper in SCRAPERS:
        logger.info(f"{Fore.CYAN}{scraper.category.upper()}'s HAS BEGUN.{Fore.RESET}")
        scraper.scrape()
        logger.info(f"{Fore.CYAN}ALL {scraper.category.upper()}'s SUCCESSFULLY SCRAPED.{Fore.RESET}")
        print(50 * f"{Fore.LIGHTWHITE_EX}*")

if __name__ == "__main__":
    run_scraper()