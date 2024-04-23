import pandas as pd

def calculate_prices(initial_price, percentage_changes):
    prices = [initial_price]
    for percentage_change in percentage_changes:
        price = prices[-1] * (1 + percentage_change)
        prices.append(price)
    return prices

def p2f(x):
    return float(x.strip('%'))/100
def recreating_upro():
    urpo_returns  = pd.read_csv('/Users/zhengkanwang/Documents/programming/notebook_testing/historical_data/UPROSIM.csv')
    initial_price = 1 # arbitrary, doesn't matter

urpo_returns  = pd.read_csv('/Users/zhengkanwang/Documents/programming/notebook_testing/historical_data/UPROSIM.csv')
urpo_returns_changes = urpo_returns['UPRO']
urpo_returns_changes = [p2f(urpo_returns_change) for urpo_returns_change in urpo_returns_changes]
prices = calculate_prices(1, urpo_returns_changes)
urpo_returns['URPO_PRICES'] = prices[1:]
print(prices)

urpo_returns.to_csv('/Users/zhengkanwang/Documents/programming/notebook_testing/historical_data/UPROSIM_WITHPRICES.csv')