from colorama import Fore
from src.core import logger
from src.utils import mark_as_completed
from src.services.scrapers import (
    BlogScraper,
    AboutScraper,
    ProgramScraper,
    ProgramTypeScraper,
)


def run_scraper() -> None:
    """
    Run the scrapers to scrape the data from the website.
    """
    scrapers = (
        BlogScraper(),
        ProgramTypeScraper(),
        AboutScraper(),
        ProgramScraper(),
    )

    for scraper in scrapers:
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
