import requests
import pandas as pd
import time
import random
import csv
import os

output_file = 'data.csv'
row_count = 0

processed_markets = set()

if os.path.exists("data.csv"):
    try:
        df_existing = pd.read_csv("data.csv")
        if "market_ticker" in df_existing.columns:
            processed_markets = set(df_existing["market_ticker"])
    except pd.errors.EmptyDataError:
        # If file exists but empty, treat as no data
        processed_markets = set()

# Get all markets for series
series_url = f"https://api.elections.kalshi.com/trade-api/v2/series"
series_response = requests.get(series_url)
series_data = series_response.json()

for series in series_data['series']:

    series_ticker = series['ticker']
    series_category = series['category']
    series_tags = series['tags']
    series_title = series['title']

    # Filter by "Politics" category
    if series_category != "Politics":
        continue

    markets_url = f"https://api.elections.kalshi.com/trade-api/v2/markets?series_ticker={series_ticker}&status=open"
    markets_response = requests.get(markets_url)
    markets_data = markets_response.json()

    markets = markets_data.get("markets")

    if markets is None:
        print("Unexpected response:", markets_data)
        continue

    
    for market in markets_data['markets']:
        

        market_ticker = market['ticker']
        if market_ticker in processed_markets:
            continue

        market_title= market['title']
        market_event_ticker = market['event_ticker']
        market_yes = market['yes_bid_dollars']
        market_no = market['no_bid_dollars']
        market_volume = market['volume']
        market_volume_24 = market['volume_24h']
        market_open_int = market['open_interest']
        market_last_price = market['last_price_dollars']
        market_prev_price = market['previous_price_dollars']
        

        
        if markets_data['markets']:
        # Get details for the market's event
            event_ticker = market['event_ticker']
            event_url = f"https://api.elections.kalshi.com/trade-api/v2/events/{event_ticker}"
            event_response = requests.get(event_url)
            event_data = event_response.json()
            time.sleep(random.uniform(0.1, 0.3))

            event_title = event_data['event']['title']
            event_category = event_data['event']['category']
            time_scraped = pd.Timestamp.now('UTC')

        row_count += 1

        # Create dictionary
        row = {
            "series_ticker": series_ticker,
            "series_category": series_category,
            "series_tags": series_tags,
            "event_category": event_category,
            "event_title": event_title,
            "market_ticker": market_ticker,
            "market_title": market_title,
            "market_event_ticker": market_event_ticker,
            "yes_bid_dollars": market_yes,
            "no_bid_dollars": market_no,
            "last_price_dollars": market_last_price,
            "previous_price_dollars": market_prev_price,
            "volume": market_volume,
            "volume_24h": market_volume_24,
            "open_interest": market_open_int,
            "time_scraped": time_scraped
        }
        df_row = pd.DataFrame([row]) # Append to row
        
        file_exists = os.path.exists(output_file)
        file_empty = (not file_exists) or os.path.getsize(output_file) == 0

        df_row.to_csv(
            output_file,
            mode="a" if file_exists else "w",
            header=file_empty,
            index=False
        )
        
        processed_markets.add(market_ticker) 
        print(f"Saved {market_ticker} | Row {row_count}")

