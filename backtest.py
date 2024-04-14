from backtesting import Backtest, Strategy
from backtesting.lib import crossover

from backtesting.test import SMA, GOOG
import pandas as pd

df = pd.read_csv('./historical_data/SPXL.csv', index_col=0, parse_dates=True, infer_datetime_format=True)
def RelfexiveIndicator(arr: pd.Series) -> pd.Series:
    """
    Returns `n`-period simple moving average of array `arr`.
    """
    return pd.Series(arr)

class SmaCross(Strategy):
    def init(self):
        self.price = self.data.Open
        self.relfexive_indicator = self.I(RelfexiveIndicator, self.price)
        self.ma = self.I(SMA, self.price, 50)
        self.index = 0

    def next(self):
        if crossover(self.relfexive_indicator, self.ma):
            self.buy()
        elif crossover(self.ma, self.relfexive_indicator):
            self.sell(size=.000000001)


bt = Backtest(df, SmaCross, commission=0, exclusive_orders=True)
stats = bt.run()
bt.plot()
print(stats)