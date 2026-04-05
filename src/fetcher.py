import yfinance as yf
import logging

logger = logging.getLogger(__name__)

def fetch_earnings_dates(ticker):
    logger.debug("function started with %s", ticker)

    try:
        stock = yf.Ticker(ticker)
        earnings_dates = stock.earnings_dates
        logger.info("stock earnings dates fetched for %s", ticker)

        if earnings_dates.empty:
            logger.warning("stock earnings dates is empty for %s", ticker)

        return earnings_dates

    except Exception as e:
        logger.exception("stock.earnings_dates failed for %s", ticker)

def fetch_price_history(ticker, start_date, end_date):
    logger.debug("function started with %s %s %s", ticker, start_date, end_date)

    try:
        stock = yf.Ticker(ticker)
        history = stock.history(start=start_date, end=end_date)
        logger.info("price history fetched for %s, %s rows returned", ticker, len(history))
        
        if history.empty:
            logger.warning("empty price history for %s from %s to %s", ticker, start_date, end_date)

        return history[["Close", "Volume"]]
    
    except Exception as e:
        logger.exception("stock.history failed for %s from %s to %s", ticker, start_date, end_date)