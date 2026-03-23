from dotenv import load_dotenv
import os

load_dotenv()

DB_NAME = os.getenv("DB_NAME","earnings_tracker.db")
PRICE_MOVE_THRESHOLD = float(os.getenv("PRICE_MOVE_THRESHOLD", 0.05))
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