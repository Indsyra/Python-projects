import csv
import os
import requests
import time
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


STOCK_PRICE_FILE = '..\\assets\\data_scraping\\stock_price.csv'
CHROME_DRIVER_PATH = 'C:\\Users\\indira\\Downloads\\chromedriver-win64 (2)\\chromedriver-win64\\chromedriver.exe'

def fetch_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Referer": "https://www.google.com/",
        "Connection": "keep-alive",
        "Cookie": "A1S=d=AQABBMkxg2gCEOog0J9j8Cna7vUBtld6K6EFEgABCAGAhGivaOWwJm0A9qMCAAcIXCqDaN7WHuM&S="
                "AQAAAiNMiidwzGx2GPkeeEGBUEo; A3=d=AQABBMkxg2gCEOog0J9j8Cna7vUBtld6K6EFEgABCAGAhGivaOWwJ"
                "m0A9qMCAAcIXCqDaN7WHuM&S=AQAAAiNMiidwzGx2GPkeeEGBUEo; EuConsent=CQVG9oAQVG9oAAOACBFRB0F"
                "oAP_gAEPgACiQKptB9G7WTXFneTp2YPskOYwX0VBJ4MAwBgCBAUABzBIUIBwGVmAzJEyIICACGAIAIGBBIABtGAh"
                "AQEAAIIAFAABIAEgAIBAAIGAAACAAAABACAAAAAAAAAAQgEAXMBQgmCYEBFoIQUhAggAgAQAAAAAEAIgBCAQAE"
                "AAAQAAACAAAACgAAgAAAAAAAAAEAFAIEAAAIAECAgvkdAAAAAAAAAAIAAYACAABAAAAAIKpgAkGhUQRFgQAhEIG"
                "EECAAQUBABQIAgAACBAAAATBAUIAwAVGAyAEAIAAAAAAAAAAABAAABAAhAAEAAAIAAAAAIAAgAIAAAACAAAAAAAA"
                "AAAAAAAAAAAAAAAAAGIBAggCAABBAAQUAAAAAgAAAAAAAAAIgACAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAIEA"
                "AAIAAAAoDEFgAAAAAAAAAAAAAACAABAAAAAIAAA; A1=d=AQABBMkxg2gCEOog0J9j8Cna7vUBtld6K6EFEgABCAG"
                "AhGivaOWwJm0A9qMCAAcIXCqDaN7WHuM&S=AQAAAiNMiidwzGx2GPkeeEGBUEo; GUC=AQABCAFohIBor0IfpASl&s"
                "=AQAAAGA4-33b&g=aIMx0w; cmp=t=1753428429&j=1&u=1---&v=90; axids=gam=y-DE7gN3hE2uJpie_Wi8Zk7"
                "mo_tp_.vu8R~A&dv360=eS1Fek01cDgxRTJ1RlgzSVp0VFRBM0lMdWlyamZjdW13UX5B&ydsp=y-yLBqfaNE2uIO2Tp"
                "8WOBUvNVDYRePtTmh~A&tbla=y-ZU_BvMlE2uLj0WbKu62ZwbqQheTARj_6~A; tbla_id=ded9f331-d753-45be-9"
                "9ba-901b8a31f351-tuctf7cb750; PRF=t%3DAAPL%26dock-collapsed%3Dtrue"
    }
    # options = Options()
    # options.add_argument("--headless")
    # options.add_argument("--disable-gpu")
    # options.add_argument("--no-sandbox")
    # options.add_argument("--window-size=1920x1080")
    # options.add_argument('--ignore-certificate-errors')
    # options.add_argument('--ignore-ssl-errors')

    # service = Service(executable_path=CHROME_DRIVER_PATH)
    # driver = webdriver.Chrome(options=options, service=service)
    
    # try:
    #     driver.get(url)

    #     try:
    #         accept = driver.find_element(By.NAME, "agree")
    #         accept.click()
    #         time.sleep(2)
    #     except:
    #         pass

    #     time.sleep(2)

    #     html = driver.page_source
    #     print(html[1000:], "\n\n", type(html))
    #     return html
    # finally:
    #     driver.quit()

    response = requests.get(url, headers=headers)
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
    url = f"https://finance.yahoo.com/quote/{ticker}/"
    html = fetch_page(url)
    if not html:
        return None

    with open(f"..\\assets\\data_scraping\\{ticker}.html", "w", encoding="utf-8") as file:
        file.write(html)

    soup = parse_html(html)
    price_tag = soup.find("span", {"data-testid": "qsp-price"})
    price_tag = price_tag if price_tag is not None else soup.find("fin-streamer", {"data-symbol": ticker, "data-field": "regularMarketPrice"})

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
                df_line = pd.DataFrame(
                    [{
                        "Date": datetime.strftime(timestamp, "%Y-%m-%d"),
                        "Time": datetime.strftime(timestamp, "%H:%M:%S"),
                        "Stock": ticker,
                        "Price": float(price)
                    }],
                )

            df = pd.concat([df, df_line], ignore_index=True)
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
