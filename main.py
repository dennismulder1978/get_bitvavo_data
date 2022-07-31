from func import price_list
import pandas as pd
import numpy as np

coin_list = ['BTC', 'ETH', 'SOL', 'ADA', 'MATIC', 'AVAX', 'SAND']
coin_price_lst = np.array([price_list(each) for each in coin_list])
# pd.DataFrame.from_records(coin_price_lst, index=coin_list).T.to_csv('name.csv')
print(pd.DataFrame.from_records(coin_price_lst, index=coin_list).T)
