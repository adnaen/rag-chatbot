from colorama import Fore

from src.scraping.blog_scraper import BlogScraper
from src.scraping.program_type_scraper import ProgramTypeScraper
from src.scraping.about_scraper import AboutScraper
from src.scraping.program_scraper import ProgramScraper
from src.config import logger
from src.config import constants


def run_scraper() -> None:
    """
    Run the scrapers to scrape the data from the website.
    Args:
        None

    Returns:
        None
    """
    SCRAPERS = (
        BlogScraper(constants.BLOG_SITEMAP_URL),
        ProgramTypeScraper(constants.PROGRAM_TYPE_SITEMAP_URL),
        AboutScraper(constants.ABOUT_SITEMAP_URL),
        ProgramScraper(constants.PROGRAM_SITEMAP_URL),
    )

    for scraper in SCRAPERS:
        try:
            logger.info(
                f"{Fore.GREEN}{scraper.category.upper()}'s HAS BEGUN.{Fore.RESET}"
            )
            scraper.scrape()
            logger.info(
                f"{Fore.GREEN}ALL {scraper.category.upper()}'s SUCCESSFULLY SCRAPED.{Fore.RESET}"
            )
            print(50 * f"{Fore.GREEN}*" + f"{Fore.RESET}")
        except KeyboardInterrupt:
            print("KeyboardInterrupt, Quitting...")
            break


if __name__ == "__main__":
    run_scraper()
