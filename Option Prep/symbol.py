from itertools import product
from expirydate import generate_expiry_date
from strikeprice import generate_strike_price

from itertools import product

def generate_symbols(ticker_set, frequency, expiration_dates, option_types, strike_prices):
    """Generate a set of option symbols based on input parameters.
    
    Parameters:
        ticker_set (set of str): Set of tickers, e.g., {"SPX"}.
        frequency (str): Expiry frequency, e.g., "W" for weekly.
        expiration_dates (set of str): Set of dates in YYMMDD format.
        option_types (list of str): List of option types, e.g., ["P", "C"].
        strike_prices (set of int): Set of strike prices as integers.
        
    Returns:
        set of str: Symbols in the format "O:SPXW241106P05700000".
    """
    symbols = set()
    
    # Generate all combinations of ticker, date, option type, and strike price
    for ticker, date, option_type, strike_price in product(ticker_set, expiration_dates, option_types, strike_prices):
        # Convert the strike price to a string without leading zeros
        strike_str = str(strike_price)
        
        # Construct the symbol
        symbol = f"O:{ticker}{frequency}{date}{option_type}0{strike_str}000"
        symbols.add(symbol)
    
    return symbols

# # Example usage
# ticker_set = {"SPX"}
# frequency = "W"
# expiration_dates = generate_expiry_date({2024},{11},{1,4,5,6,7,8})
# option_types = ["P", "C"]  # Use "P" and "C" to avoid the extra zero
# strike_prices = generate_strike_price(5700)

# symbols = generate_symbols(ticker_set, frequency, expiration_dates, option_types, strike_prices)
# print("Generated Symbols:", symbols)
