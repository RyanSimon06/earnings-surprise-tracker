import logging
from dotenv import load_dotenv
import os

logger = logging.getLogger(__name__)

dotenv_loaded = load_dotenv()

if dotenv_loaded:
    logger.debug(".env file loaded successfully")
else:
    logger.warning("no .env file found, using default values")

DB_NAME = os.getenv("DB_NAME", "earnings_tracker.db")
PRICE_MOVE_THRESHOLD = float(os.getenv("PRICE_MOVE_THRESHOLD", 0.05))

logger.debug("DB_NAME set to %s", DB_NAME)
logger.debug("PRICE_MOVE_THRESHOLD set to %s", PRICE_MOVE_THRESHOLD)

STOCKS = [
    ("AAPL", "Apple Inc.", "Technology"),
    ("MSFT", "Microsoft Corp.", "Technology"),
    ("GOOGL", "Alphabet Inc.", "Technology"),
    ("META", "Meta Platforms", "Technology"),
    ("NVDA", "NVIDIA Corp.", "Technology"),
    ("JPM", "JPMorgan Chase", "Finance"),
    ("BAC", "Bank of America", "Finance"),
    ("GS", "Goldman Sachs", "Finance"),
    ("JNJ", "Johnson & Johnson", "Healthcare"),
    ("PFE", "Pfizer Inc.", "Healthcare"),
    ("AMZN", "Amazon.com Inc.", "Consumer"),
    ("WMT", "Walmart Inc.", "Consumer"),
    ("MCD", "McDonald's Corp.", "Consumer"),
    ("XOM", "ExxonMobil Corp.", "Energy"),
    ("CVX", "Chevron Corp.", "Energy"),
    ("CAT", "Caterpillar Inc.", "Industrial"),
    ("BA", "Boeing Co.", "Industrial"),
    ("VZ", "Verizon Communications", "Telecoms"),
    ("T", "AT&T Inc.", "Telecoms"),
    ("NEE", "NextEra Energy", "Utilities"),
]

logger.debug("%s stocks configured", len(STOCKS))