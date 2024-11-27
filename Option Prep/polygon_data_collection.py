from polygon import RESTClient
import pandas as pd
import info
from symbol import generate_symbols  
from strikeprice import generate_strike_price
from expirydate import generate_expiry_date
import os

client = RESTClient(info.api_key)

# Define the parameters for symbol generation
ticker_set = {"SPX"}
frequency = "W"
expiration_dates = generate_expiry_date({2024}, {11}, {7})
option_types = ["P", "C"]  # Both call and put options
strike_prices = generate_strike_price(5620)

# Generate symbols
symbols = generate_symbols(ticker_set, frequency, expiration_dates, option_types, strike_prices)

# Define date range for aggregation
start_date = "2024-10-28"
end_date = "2024-11-08"
interval_minutes = 5  # 5-minute intervals

# Loop through each symbol and fetch data
for symbol in symbols:
    print(f"Fetching data for symbol: {symbol}")
    aggs = []
    
    # Fetch aggregated data for the current symbol
    for a in client.list_aggs(
        symbol,                    # Symbol for the S&P 500 option
        interval_minutes,          # 5-minute intervals
        "minute",                  # Frequency of aggregation
        start_date,                # Start date
        end_date,                  # End date
        limit=50000,
    ):
        # Append each aggregation as a dictionary
        aggs.append({
            "symbol": symbol,
            "timestamp": a.timestamp,
            "open": a.open,
            "high": a.high,
            "low": a.low,
            "close": a.close,
            "volume": a.volume,
            "transactions": a.transactions
        })
    
    # Convert the data for this symbol to a DataFrame
    df = pd.DataFrame(aggs)
    
    # Save DataFrame to CSV with the symbol name
    file_name = f"{symbol}.csv"
    df.to_csv(file_name, index=False)
    print(f"Data for {symbol} saved to {file_name}")
