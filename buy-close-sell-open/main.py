# region imports
from AlgorithmImports import *
# endregion

class BuyclosesellOpen(QCAlgorithm):

    def Initialize(self):
        # Locally Lean installs free sample data, to download more data please visit https://www.quantconnect.com/docs/v2/lean-cli/datasets/downloading-data
        self.SetStartDate(2010, 10, 7)  # Set Start Date
        self.SetEndDate(2024, 10, 11)  # Set End Date
        self.SetCash(100000)  # Set Strategy Cash
        self.SetWarmUp(30)
        self.AddEquity("SPXL", Resolution.Daily)
        self.symbol = self.AddEquity("SPXL", Resolution.Daily).Symbol
        self.sma = self.SMA(self.symbol, 30)

    def OnData(self, data: Slice):
        """OnData event is the primary entry point for your algorithm. Each new data point will be pumped in here.
            Arguments:
                data: Slice object keyed by symbol containing the stock data
        """
        price = data[self.symbol].Price
        if self.sma.Current.Value >= price:
            self.SetHolds(self.symbol, 0)
        else:
            self.SetHoldings(self.symbol,1)
