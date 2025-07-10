**3D Volatility Surface Construction for SPX American Options**


This project constructs and analyzes a 3D volatility surface for SPX American options during the 2024 U.S. presidential election period (October 28 to November 8, 2024). It leverages real market data, Monte Carlo simulations, and advanced stochastic models to enhance option pricing accuracy and risk assessment.

Project Highlights
Volatility Surface Modeling:
Built a 3D implied volatility surface across multiple strike prices and daily expiries, using Black-Scholes pricing and real SPX option data.

Monte Carlo Simulation:
Simulated 10,000 SPX price paths at 5-minute intervals using both Geometric Brownian Motion (GBM) and advanced models like Heston and CGMY.

American Option Focus:
Daily expiries captured through American-style option data to reflect realistic and short-term trading behavior.

Volatility Analysis During Uncertainty:
Focused on the election period, known for high market volatility, to evaluate model robustness under real-world stress.

Models Used
Black-Scholes Model:
Used for initial pricing and implied volatility calculation.

Geometric Brownian Motion (GBM):
Simulated base case price paths.

Heston Model:
Added stochastic volatility to better reflect real market dynamics.

CGMY Model:
Incorporated jump diffusion to simulate fat tails and high uncertainty.

Project Structure


├── data/
│   └── spx_historical_data.csv          # 5-min SPX price data
│   └── real_option_data.csv             # Real option chain (strike, expiry, prices)
├── simulated_price_paths.csv            # Simulated SPX price paths
├── implied_volatilities.csv             # Raw implied volatility data
├── implied_volatilities_final_cleaned.csv
├── monte_carlo_simulation.py            # GBM-based price simulation
├── heston_simulation.py                 # Heston model implementation
├── cgmy_simulation.py                   # CGMY jump diffusion model
├── black_scholes.py                     # Black-Scholes option pricing
├── calculate_implied_volatility.py      # Newton-Raphson IV calculation
└── README.md                            # You're here!

Visualization
Plots of simulated SPX paths under each model

3D volatility surface using strike vs. expiry vs. implied volatility

Comparisons between real and simulated surfaces

Technologies
Python (NumPy, Pandas, Matplotlib, SciPy, Seaborn)

statsmodels (for stationarity testing)

Monte Carlo Simulation

Numerical methods (Newton-Raphson)

Future Enhancements
Incorporate early exercise premium for American options.

Calibrate Heston and CGMY parameters directly from historical SPX data.

Build real-time volatility tracking dashboard with live data.



