import yfinance as yf
import pandas as pd

# Define the ticker symbol for S&P 500 (Yahoo Finance uses "^GSPC" for the S&P 500 index)
ticker = "^GSPC"

# Fetch historical data
# Start and end dates can be adjusted as needed
start_date = "2024-09-20"
end_date = "2024-10-28"
spx_data = yf.download(ticker, start=start_date, end=end_date, interval="5m")

# Save to CSV for future use
file_path = "spx_historical_data.csv"
spx_data.to_csv(file_path)
print(f"Historical data saved to {file_path}")

# Display the first few rows to ensure the data is downloaded correctly
#print(spx_data.head())

#########################################################
# Load the data
file_path = 'spx_historical_data.csv'
spx_data = pd.read_csv(file_path)

# Drop the first row (0th index)
spx_data = spx_data.drop(0)

# Drop the first row (index 1) and reset the index
spx_data = spx_data.drop(index=1).reset_index(drop=True)
spx_data = spx_data.rename(columns={'Price': 'Datetime'})

# Ensure numeric columns are correctly parsed
numeric_columns = ['Adj Close', 'Close', 'High', 'Low', 'Open', 'Volume']
spx_data[numeric_columns] = spx_data[numeric_columns].apply(pd.to_numeric, errors='coerce')

# Convert "Datetime" column to a proper datetime object
spx_data['Datetime'] = pd.to_datetime(spx_data['Datetime'])

spx_data.set_index('Datetime', inplace=True)
# Display the cleaned dataset

# Sort index from oldest to newest
df = spx_data.sort_index()

# Save the cleaned data for future reference
df.to_csv("spx_historical_data.csv", index=True)
print("Cleaned 5-minute data saved to spx_historical_data.csv")


print(df.head())
