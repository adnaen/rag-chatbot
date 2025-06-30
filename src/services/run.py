from colorama import Fore
from src.core import logger, Settings
from src.utils import mark_as_completed
from src.services.scrapers.blogs import BlogScraper
from src.services.scrapers.about import AboutScraper
from src.services.scrapers.programs import ProgramScraper
from src.services.scrapers.program_types import ProgramTypeScraper


def run_scraper() -> None:
    """
    Run the scrapers to scrape the data from the website.
    Args:
        None

    Returns:
        None
    """
    SCRAPERS = (
        BlogScraper(Settings.BLOG_SITEMAP_URL),
        ProgramTypeScraper(Settings.PROGRAM_TYPE_SITEMAP_URL),
        AboutScraper(Settings.ABOUT_SITEMAP_URL),
        ProgramScraper(Settings.PROGRAM_SITEMAP_URL),
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
    mark_as_completed("data_ingestion")


if __name__ == "__main__":
    run_scraper()
