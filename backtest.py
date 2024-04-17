from backtesting import Backtest
import pandas as pd

from backtest.strategies import Sma50Cross, BuyAndHold

df = pd.read_csv('./historical_data/SPXL.csv', index_col=0, parse_dates=True, infer_datetime_format=True)

df = df.loc[('2009-06-30' < df.index) & (df.index < '2021-01-01')]
df['Close'] = df['Open']
bt = Backtest(df, BuyAndHold, commission=0, exclusive_orders=True, trade_on_close=True)
stats = bt.run()
# stats._equity_curve.to_csv('/Users/zhengkanwang/Documents/programming/notebook_testing/output/sma_50')
bt.plot()
print(stats)