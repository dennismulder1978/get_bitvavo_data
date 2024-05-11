import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from datetime import datetime as dt

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
            euro = df.iloc[each, 0] * coin
            coin = 0
    
    # final result in Euro
    if euro == 0:
        euro = df.iloc[-1, 0] * coin
    
    return euro


def initiate_coin_test():    
    end_result = []
    index_future = []
    index_buy_prec = []
    index_sell_prec = []
    result_i = []
    for i in range(1, 12, 1):
        index_future.append(i)
        print(f"|{i}|", end="")
        # create appropriate DataFrame
        luna2_dataframe = create_df(shift=i)
        
        # Testing with a smaller database. 
        # luna2_dataframe = luna2_dataframe[:100]
        
        # per DataFrame, loop through all buy percentages
        result_j = []
        for jj in range(2, 5, 1):
            print(".", end="")
            j = jj/2
            index_buy_prec.append(j)
            result_k = []
            # per buy percentage loop through all sell percentages
            for kk in range(-2,-5,-1):
                k = kk/2
                index_sell_prec.append(k)
                result_k.append(coin_test(df=luna2_dataframe, sell_perc=k, buy_perc=j))
            
            result_j.append(result_k)
            result_k = []
        
        result_i.append(result_j)
        result_j = []
        
    end_result.append(result_i)

    print("\n--------------------------")
    end_result_array = np.array(result_i)

    save_name = 'end_result_array__' + dt.strftime(dt.now(), "%H_%M_%d_%m_%y")
    np.save(save_name, end_result_array)

    max = np.unravel_index(end_result_array.argmax(), end_result_array.shape)
    print(f'Max result: Euro:{end_result_array.max():.2f}, cohort: {index_future[max[0]]}, buy percentage: {index_buy_prec[max[1]]}, sell percentage: {index_sell_prec[max[2]]}')
    
    return end_result_array


def show_3d_result():
    res = np.load('end_result_array_1.npy')
    indexes = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5]
    cohort_index = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120]
    
    max = np.unravel_index(res.argmax(), res.shape)
    print(f'Max result: Euro:{res.max():.2f}, cohort: {cohort_index[max[0]]}, buy percentage: {indexes[max[1]]}, sell percentage: {indexes[max[2]]}')
    
    
    return res


era = initiate_coin_test()
print(f'ERA (initial): {era.shape}')
