# Understanding web scraping Basics
# Process of extracting data from a website

import requests
from bs4 import BeautifulSoup
import time


def fetch_page(url):
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    # }
    # response = requests.get(url, headers=headers)
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    elif response.status_code == 429:
        print("Too many requests - try again later.")
        return None
    else:
        print(f"Failed to fetch page: {response.status_code}")
        return None


# Using requests and BeautifulSoup for Scraping
def parse_html(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup


# Extracting Stock Prices
def get_stock_price(ticker):
    url = f"https://finance.yahoo.com/quote/{ticker}/"
    html = fetch_page(url)
    if not html:
        return None
    soup = parse_html(html)
    # price_tag = soup.find("fin-streamer", {"data-symbol": ticker, "data-field": "regularMarketPrice"})
    price_tag = soup.find("span", {"data-testid": "qsp-price"})
    if price_tag:
        return price_tag.text
    else:
        print("Stock price not found")
        return None


ticker = "AAPL"


# Dynamic Updates for Real-Time Tracking
def track_stock_price(ticker, interval=60):
    while True:
        price = get_stock_price(ticker)
        if price:
            print(f"The current price of {ticker} is ${price}")
        time.sleep(interval)


track_stock_price(ticker)
