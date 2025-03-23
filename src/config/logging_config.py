import logging
import sys
from colorama import Fore


fmt = f"{Fore.GREEN} %(asctime)s %(levelname)s %(module)s {Fore.RESET} %(message)s"

logging.basicConfig(
    format=fmt, level=logging.INFO, handlers=[logging.StreamHandler(sys.stdout)]
)

logger = logging.getLogger("AppLogger")
