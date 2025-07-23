import csv
import os
import requests
import time
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime



STOCK_PRICE_FILE = '..\\assets\\data_scraping\\stock_price'

def fetch_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    response = requests.get(url, headers)
    if response.status_code == 200:
        return response.text
    elif response.status_code == 429:
        print("Too many requests - try again later.")
        return None
    else:
        print(f"Failed to fetch the page: {response.status_code}")


def parse_html(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup


def get_stock_price(ticker):
    url = f"https://finance.yahoo.com/quote/{ticker}"
    html = fetch_page(url)
    if not html:
        return None

    soup = parse_html(html)
    price_tag = soup.find("span", {"data-testid": "qsp-price"})
    if price_tag:
        return price_tag.text
    else:
        print(f"Stock price not found for ticker {ticker}.")
        return None


def track_stock_price(tickers, interval=60):
    while True:
        try:
            df = pd.read_csv(STOCK_PRICE_FILE)
        except Exception:
            df = pd.DataFrame(columns=[
                'Date', 'Time', 'Stock', 'Price'
                ]
            )
        prices = [get_stock_price(ticker) for ticker in tickers]
        for ticker, price in zip(tickers, prices):
            if price:
                print(f"{ticker}: ${price}")
                timestamp = datetime.now()
                df.append(
                    {
                        "Date": datetime.strftime(timestamp, "%Y-%m-d"),
                        "Time": datetime.strftime(timestamp, "%H:%M:%S"),
                        "Stock": ticker,
                        "Price": float(price)
                    },
                    ignore_index=True
                )
            df.to_csv(STOCK_PRICE_FILE, index=False)
        time.sleep(interval)


def main():
    print("Welcome to the Stock Price Tracker!")
    tickers = input("Enter the list of stocker tickers symbols separated by a space (e.g, AAPL TSLA IQVF): ").upper().split(" ")
    interval = int(input("Enter the update interval (in seconds): "))
    print(f"Tracking stock prices for [{', '.join(tickers)}] every {interval} seconds...")
    track_stock_price(tickers, interval)


if __name__ == "__main__":
    main()
