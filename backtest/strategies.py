import logging

import pandas as pd
from backtesting import Strategy
from backtesting.lib import crossover
from backtesting.test import SMA


def RelfexiveIndicator(arr: pd.Series) -> pd.Series:
    """
    Returns `n`-period simple moving average of array `arr`.
    """
    return pd.Series(arr)


class Sma2Cross(Strategy):
    def init(self):
        self.price = self.data.Open
        self.relfexive_indicator = self.I(RelfexiveIndicator, self.price)
        self.ma = self.I(SMA, self.price, 2)
        self.index = 1
        self.starting_index = 1

    def next(self):
        if self.index == self.starting_index:
            if self.ma < self.relfexive_indicator:
                self.buy()
                logging.info(
                    "the date is {} and the RI is {} and the ma is {} and we had a buy for the first period".format(
                        self.data.index[self.index], self.relfexive_indicator[-1], self.ma[-1]))
                print("the date is {} and the RI is {} and the ma is {} and we had a buy for the first period".format(
                    self.data.index[self.index], self.relfexive_indicator[-1], self.ma[-1]))
            else:
                self.position.close()
        if crossover(self.relfexive_indicator, self.ma):
            self.buy()
            logging.info("the date is {} and the RI is {} and the ma is {} and we had a buy crossover".format(
                self.data.index[self.index], self.relfexive_indicator[-1], self.ma[-1]))
            print("the date is {} and the RI is {} and the ma is {} and we had a buy crossover".format(
                self.data.index[self.index], self.relfexive_indicator[-1], self.ma[-1]))
        elif crossover(self.ma, self.relfexive_indicator):
            self.position.close()
            logging.info("the date is {} and the RI is {} and the ma is {} and we had a sell crossover".format(
                self.data.index[self.index], self.relfexive_indicator[-1], self.ma[-1]))
            print("the date is {} and the RI is {} and the ma is {} and we had a sell crossover".format(
                self.data.index[self.index], self.relfexive_indicator[-1], self.ma[-1]))
        self.index += 1


class Sma200Cross(Strategy):
    def init(self):
        self.price = self.data.Open
        self.relfexive_indicator = self.I(RelfexiveIndicator, self.price)
        self.ma = self.I(SMA, self.price, 200)
        self.index = 199
        self.starting_index = 199

    def next(self):
        # need this because it doesn't crossover during the first calculation of the MA, so need this to buy
        # during the first calculation.
        if self.index == self.starting_index:
            if self.ma < self.relfexive_indicator:
                self.buy()
                logging.error(
                    "the date is {} and the RI is {} and the ma is {} and we had a buy for the first period".format(
                        self.data.index[self.index], self.relfexive_indicator[-1], self.ma[-1]))
            else:
                self.position.close()
        if crossover(self.relfexive_indicator, self.ma):
            self.buy()
            logging.info("the date is {} and the RI is {} and the ma is {} and we had a buy crossover".format(
                self.data.index[self.index], self.relfexive_indicator[-1], self.ma[-1]))
        elif crossover(self.ma, self.relfexive_indicator):
            self.position.close()
            logging.info("the date is {} and the RI is {} and the ma is {} and we had a sell crossover".format(
                self.data.index[self.index], self.relfexive_indicator[-1], self.ma[-1]))
        self.index += 1

class Sma50Cross(Strategy):
    def init(self):
        self.price = self.data.Open
        self.relfexive_indicator = self.I(RelfexiveIndicator, self.price)
        self.ma = self.I(SMA, self.price, 50)
        self.index = 49
        self.starting_index = 49

    def next(self):
        # need this because it doesn't crossover during the first calculation of the MA, so need this to buy
        # during the first calculation.
        if self.index == self.starting_index:
            if self.ma < self.relfexive_indicator:
                self.buy()
                logging.error(
                    "the date is {} and the RI is {} and the ma is {} and we had a buy for the first period".format(
                        self.data.index[self.index], self.relfexive_indicator[-1], self.ma[-1]))
            else:
                self.position.close()
        if crossover(self.relfexive_indicator, self.ma):
            self.buy()
            logging.info("the date is {} and the RI is {} and the ma is {} and we had a buy crossover".format(
                self.data.index[self.index], self.relfexive_indicator[-1], self.ma[-1]))
        elif crossover(self.ma, self.relfexive_indicator):
            self.position.close()
            logging.info("the date is {} and the RI is {} and the ma is {} and we had a sell crossover".format(
                self.data.index[self.index], self.relfexive_indicator[-1], self.ma[-1]))
        self.index += 1

class BuyAndHold(Strategy):
    def init(self):
        self.price = self.data.Open
        self.relfexive_indicator = self.I(RelfexiveIndicator, self.price)
        self.ma = self.I(SMA, self.price, 2)
        self.index = 0
        self.starting_index = 0

    def next(self):
        if self.index == self.starting_index:
            self.buy()
            self.index += 1
        else:
            self.index += 1
            pass
