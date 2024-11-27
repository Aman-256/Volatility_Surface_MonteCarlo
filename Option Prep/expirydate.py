from itertools import product

def generate_expiry_date(years, months, days):
    """Generate a set of expiration dates in YYMMDD format from input years, months, and days.
    
    Parameters:
        years (set of int): Set of years (e.g., {2024, 2025}).
        months (set of int): Set of months (e.g., {10, 11}).
        days (set of int): Set of days (e.g., {28, 29}).
        
    Returns:
        set of str: Expiration dates in 'YYMMDD' string format.
    """
    expiry_date = set()
    
    # Use product to create combinations of years, months, and days
    for year, month, day in product(years, months, days):
        # Format each date as YYMMDD
        year_str = str(year)[-2:]  # Take the last two digits of the year
        month_str = f"{month:02}"  # Zero-pad month to two digits
        day_str = f"{day:02}"      # Zero-pad day to two digits
        expiry_date.add(f"{year_str}{month_str}{day_str}")
    
    return expiry_date

## Example usage
# years = {2024}
# months = {10, 11}
# days = {28,29,30}
# expiration_dates = generate_expiry_date(years, months, days)
# print("Generated Expiration Dates:", expiration_dates)
