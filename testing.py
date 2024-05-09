import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt


def create_df(shift:int=2):
    """
    Creates a processed DataFrame from the LUNA2 trade data with adjusted columns.

    Args:
        shift (int, optional): The number of shifts to apply to calculate the target value. Defaults to 2.

    Returns:
        pandas.DataFrame: Processed DataFrame with adjusted columns from the LUNA2 trade data.
    """

    LUNA2 = pd.read_csv('./results/LUNA2_trade_data__per_5m__168343_items__created_08-May-2024_22-01.csv')
    LUNA2 = LUNA2.iloc[::-1]
    LUNA2 = LUNA2.reset_index(drop=True)
    LUNA2["Target"] = LUNA2["Close"].shift(-shift)
    LUNA2["change"] = LUNA2["Target"] - LUNA2["Close"]
    LUNA2["change_perc"] = ((LUNA2["Target"] - LUNA2["Close"])/LUNA2["Close"]) * 100
    LUNA2["Vol_adjusted"] = (LUNA2["Vol."] / LUNA2["Vol."].mean()) / 100
    LUNA2 = LUNA2.dropna()
    LUNA2 = LUNA2.drop(["Open", "High", "Low", "Date", "Vol.", "change", "Vol_adjusted", "Target"], axis=1)

    return LUNA2


def coin_test(df: pd.DataFrame, sell_perc:int=-1, buy_perc:int=1):    
    coin = 0
    euro = 100
    counter = 0
    for each in range(df.shape[0]):
        if (df.iloc[each, 1] > buy_perc) & (coin == 0):
            coin = euro / df.iloc[each, 0]
            euro = 0
            counter += 1
        elif (df.iloc[each, 1] < sell_perc) & (euro == 0):
            euro = df.iloc[each, 1] * coin
            coin = 0

    print(f'Counter: {counter}')
    if euro == 0:
        euro = df.iloc[-1, 0] * coin
    return euro
    

for i in range(120,140,6):
    print(f'Shift {float(i/12)} uur: {coin_test(df=create_df(shift=i), sell_perc=-3, buy_perc=3)}')



# adding target price