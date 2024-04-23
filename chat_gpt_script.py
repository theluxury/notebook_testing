import yfinance as yf

def backtest_strategy(ticker_symbol):
    # Download historical data for the ticker symbol
    ticker_data = yf.download(ticker_symbol, start="2020-01-01", end="2024-01-01")

    # Calculate VIX (Volatility Index) using historical data
    ticker_data['VIX'] = ticker_data['Close'].rolling(window=20).std() * (252 ** 0.5) * 100

    # Initialize variables for tracking trades and capital
    capital = 10000  # starting capital
    shares = 0
    buy_price = 0
    cagr = 0

    # Define the strategy
    for index, row in ticker_data.iterrows():
        if row['VIX'] < 3200 and shares == 0:
            # Buy TQQQ
            shares = capital // row['Close']
            buy_price = row['Close']
            capital -= shares * buy_price
        elif row['VIX'] > 32 and shares > 0:
            # Sell TQQQ
            capital += shares * row['Close']
            shares = 0
            cagr = (capital / 10000) ** (1 / ((index - ticker_data.index[0]).days / 365.25)) - 1

    return cagr

if __name__ == "__main__":
    ticker_symbol = "TQQQ"
    strategy_cagr = backtest_strategy(ticker_symbol)
    print("Compound Annual Growth Rate (CAGR): {:.2%}".format(strategy_cagr))
