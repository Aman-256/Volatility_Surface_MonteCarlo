def generate_strike_price(market_price, step=20, percentage_range=0):
    """Generate a list of strike prices around the market price.
    
    Parameters:
        market_price (float): The current market price of the underlying asset.
        step (int): The step size for rounding, typically 20.
        percentage_range (int): The percentage range above and below the market price.
    
    Returns:
        list of int: Strike prices as integers, rounded to the nearest multiple of `step`.
    """
    # Calculate the lower and upper bounds based on the percentage range
    lower_bound = market_price * (1 - percentage_range / 100)
    upper_bound = market_price * (1 + percentage_range / 100)
    
    # Generate strike prices within the range, rounding to the nearest multiple of `step`
    strike_price = []
    current_strike = int(lower_bound // step * step)
    
    while current_strike <= upper_bound:
        strike_price.append(current_strike)
        current_strike += step
    
    return strike_price

# # Example usage
# market_price = 5700  # Example market price for S&P 500
# strikes = generate_strike_price(market_price)
# print("Generated Strike Prices:", strikes)
