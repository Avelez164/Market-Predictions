# Library to import real-time UTC
from datetime import datetime, timedelta

# Library to call yahoo's historical data
import yfinance as yahoo

# Library to handle and use financial data
import pandas as pd

# ML file
from ML_Predictions import *


class Stock():

  def __init__(self, stock):
    self.stock = stock

  # Returns the current price of the Stock
  def currentPrice(self):
    stock_stat = yahoo.Ticker(self.stock)
    return stock_stat.info['ask']

  # Returns the # of shares
  def stockCount(self):
    return yahoo.Ticker(self.stock).info.get('sharesOutstanding', 'N/A')

  def percentage(self):
        try:
            # Retrieve historical data for the past day
            current_date = datetime.now().strftime('%Y-%m-%d')
            one_day_prior = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

            historical_data = yahoo.download(self.stock, start=one_day_prior, end=current_date)

            # Calculate percentage change
            if not historical_data.empty:
                previous_close = historical_data.iloc[0]['Close']
                current_close = self.currentPrice()
                percentage_change = ((current_close - previous_close) / previous_close) * 100
                return percentage_change
            else:
                return "No historical data available for calculating percentage change"
        except Exception as e:
            return f"Error occurred: {e}"
  # Returns Market Cap
  def marketCap(self):
    try:
      stock_data = yahoo.Ticker(self.stock)
      info = stock_data.info
      market_cap = info.get('marketCap', None)
      return market_cap
    except Exception:
      return -1

  # Calls the historical data of stock
  # 1 weeks worth of data
  def historyCall(self):

    # Obtains the current date and time (UTC)
    # Also obtains the date and time 1 week before
    current_date = datetime.now()
    one_week_prior = current_date - timedelta(days=30)

    historical_data = yahoo.download(self.stock,
                                     start=one_week_prior,
                                     end=current_date)

    return historical_data
