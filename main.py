from func import *
import pandas as pd
import numpy as np

coin_list = ['BTC', 'ETH', 'ADA', 'MATIC', 'AVAX', 'SOL']
coin_price_lst = np.array([price_list(each) for each in coin_list])
a = pd.DataFrame.from_records(coin_price_lst, index=coin_list)
# create_csv(coin_price_lst)

a.to_csv('test1.csv')