import datetime

from backtesting import Backtest
import pandas as pd

from backtest.strategies import Sma50Cross, Sma200Cross, BuyAndHold, Sma100Cross

df = pd.read_csv('./historical_data/SPXL.csv', index_col=0, parse_dates=True, infer_datetime_format=True)

# df = df.loc[(datetime.datetime.strptime('2009-07-01', '%Y-%m-%d') <= df.index & (datetime.datetime.strptime('2021-01-01', '%Y-%m-%d') > df.index)]
df = df[(df.index >= datetime.datetime.strptime('2008-06-01', '%Y-%m-%d')) & (df.index <= datetime.datetime.strptime('2021-01-01', '%Y-%m-%d'))]
# open = close means you trade on close
df['Open'] = df['Close']
bt = Backtest(df,Sma100Cross, commission=0, exclusive_orders=True, trade_on_close=True)
stats = bt.run()
# stats._equity_curve.to_csv('/Users/zhengkanwang/Documents/programming/notebook_testing/output/SSO_200_ma.csv')
bt.plot()
print(stats)