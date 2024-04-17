import logging
import math

import pandas as pd
from backtesting import Backtest

from backtest.strategies import Sma2Cross


def test_sma_cross_strategy_winning():
    d = {'Date': [
        '2020-01-01',
        '2020-01-02',
        '2020-01-03',
        '2020-01-04',
        '2020-01-05',
        '2020-01-06',

    ], 'Open': [
        1,
        2,
        3,
        4,
        5,
        4],
        'High': [0] * 6,
        'Low': [0] * 6,
        'Close': [
            1,
            2,
            3,
            4,
            5,
            4],
        'Volume': [0] * 6,
    }

    df = pd.DataFrame(data=d)
    bt = Backtest(df, Sma2Cross, commission=0, exclusive_orders=True, trade_on_close=True)
    stats = bt.run()
    assert (math.isclose(stats['Equity Final [$]'], 20000, rel_tol=.001))
    assert (math.isclose(stats['Return [%]'], 100, rel_tol=.001))
    assert (math.isclose(stats['Buy & Hold Return [%]'], 300, rel_tol=.001))
    assert (math.isclose(stats['Max. Drawdown [%]'], -20, rel_tol=.001))

def test_sma_cross_strategy_losing():
    d = {'Date': [
        '2020-01-01',
        '2020-01-02',
        '2020-01-03',
    ], 'Open': [
        10,
        20,
        10],
        'High': [0] * 3,
        'Low': [0] * 3,
        'Close': [
            10,
            20,
            10,],
        'Volume': [0] * 3,
    }
    df = pd.DataFrame(data=d)
    bt = Backtest(df, Sma2Cross, commission=0, exclusive_orders=True, trade_on_close=True)
    stats = bt.run()
    assert (math.isclose(stats['Equity Final [$]'], 5000, rel_tol=.01))
    assert (math.isclose(stats['Return [%]'], -50, rel_tol=.01))
    assert (math.isclose(stats['Buy & Hold Return [%]'],0, rel_tol=.01))
    assert (math.isclose(stats['Max. Drawdown [%]'], -50, rel_tol=.01))

def test_sma_coss_strategy_win_then_lose_buy_full_equity():
    d = {'Date': [
        '2020-01-01',
        '2020-01-02',
        '2020-01-03',
        '2020-01-04',
        '2020-01-05',
        '2020-01-06',
        '2020-01-07',
        '2020-01-08',
        '2020-01-09',

    ], 'Open': [
        1,
        1.00001,
        2,
        3,
        4,
        5,
        4,
        5,
        2.5],
        'High': [0] * 9,
        'Low': [0] * 9,
        'Close': [
            1,
            1.00001,
            2,
            3,
            4,
            5,
            4,
            5,
            2.5],
        'Volume': [0] * 9,
    }
    df = pd.DataFrame(data=d)
    bt = Backtest(df, Sma2Cross, commission=0, exclusive_orders=True, trade_on_close=True)
    stats = bt.run()
    assert (math.isclose(stats['Equity Final [$]'], 20000, rel_tol=.001))
    assert (math.isclose(stats['Return [%]'], 100, rel_tol=.001))
    assert (math.isclose(stats['Buy & Hold Return [%]'], 150, rel_tol=.001))
    # it's 60% because at one point, you had it at 50k, now 20k
    assert (math.isclose(stats['Max. Drawdown [%]'], -(50-20)*100/50, rel_tol=.001))